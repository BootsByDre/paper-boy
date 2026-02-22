"""
Celery tasks for newsletter delivery.

Pipeline:
  1. `check_due_newsletters` — runs hourly, finds newsletters due for delivery
  2. `generate_digest` — generates AI digest for a single newsletter
  3. `send_digest` — emails a ready digest to the subscriber
"""

import logging
from datetime import timedelta

from celery import shared_task
from django.utils import timezone

logger = logging.getLogger(__name__)

CADENCE_DELTA = {
    "daily": timedelta(days=1),
    "weekly": timedelta(weeks=1),
    "biweekly": timedelta(weeks=2),
    "monthly": timedelta(days=30),
}


@shared_task
def check_due_newsletters():
    """Hourly beat task — enqueues generation for any newsletter past its cadence."""
    from apps.newsletters.models import Newsletter

    now = timezone.now()
    due = []

    for newsletter in Newsletter.objects.filter(is_active=True).select_related("owner"):
        delta = CADENCE_DELTA[newsletter.cadence]
        last = newsletter.last_delivered_at or (now - delta)
        if now >= last + delta:
            due.append(newsletter.id)

    for nid in due:
        generate_digest.delay(nid)

    logger.info("Enqueued %d newsletter(s) for generation.", len(due))
    return due


@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def generate_digest(self, newsletter_id: int):
    """Generate an AI digest for the given newsletter and hand off to send_digest."""
    from apps.newsletters.models import Digest, Newsletter

    try:
        newsletter = Newsletter.objects.get(pk=newsletter_id, is_active=True)
    except Newsletter.DoesNotExist:
        logger.warning("Newsletter %s not found or inactive — skipping.", newsletter_id)
        return

    now = timezone.now()
    window_start = newsletter.last_delivered_at or (now - CADENCE_DELTA[newsletter.cadence])

    digest = Digest.objects.create(
        newsletter=newsletter,
        status=Digest.Status.GENERATING,
        window_start=window_start,
        window_end=now,
    )

    try:
        from .pipeline import build_digest

        html, text, sources = build_digest(newsletter.topic, window_start, now)
        digest.content_html = html
        digest.content_text = text
        digest.raw_sources = sources
        digest.status = Digest.Status.READY
        digest.save()
        send_digest.delay(digest.id)
    except Exception as exc:
        digest.status = Digest.Status.FAILED
        digest.error = str(exc)
        digest.save()
        raise self.retry(exc=exc)


@shared_task(bind=True, max_retries=3, default_retry_delay=30)
def send_digest(self, digest_id: int):
    """Email a ready digest to the newsletter owner."""
    from django.core.mail import send_mail
    from django.utils import timezone

    from apps.newsletters.models import Digest

    try:
        digest = Digest.objects.select_related("newsletter__owner").get(
            pk=digest_id, status=Digest.Status.READY
        )
    except Digest.DoesNotExist:
        logger.warning("Digest %s not found or not ready — skipping.", digest_id)
        return

    owner = digest.newsletter.owner

    try:
        send_mail(
            subject=f"Your {digest.newsletter.cadence} digest: {digest.newsletter.name}",
            message=digest.content_text,
            from_email=None,  # uses DEFAULT_FROM_EMAIL
            recipient_list=[owner.email],
            html_message=digest.content_html,
            fail_silently=False,
        )
        digest.status = Digest.Status.SENT
        digest.sent_at = timezone.now()
        digest.newsletter.last_delivered_at = digest.sent_at
        digest.save()
        digest.newsletter.save(update_fields=["last_delivered_at"])
        logger.info("Digest %s sent to %s.", digest_id, owner.email)
    except Exception as exc:
        raise self.retry(exc=exc)
