from django.conf import settings
from django.db import models


class Newsletter(models.Model):
    class Cadence(models.TextChoices):
        DAILY = "daily", "Daily"
        WEEKLY = "weekly", "Weekly"
        BIWEEKLY = "biweekly", "Bi-weekly"
        MONTHLY = "monthly", "Monthly"

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="newsletters",
    )
    name = models.CharField(max_length=200)
    topic = models.TextField(
        help_text="Describe the topic or topics you want covered. Be as specific as you like."
    )
    cadence = models.CharField(max_length=20, choices=Cadence.choices, default=Cadence.WEEKLY)
    is_active = models.BooleanField(default=True)
    last_delivered_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.owner.email})"


class Digest(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        GENERATING = "generating", "Generating"
        READY = "ready", "Ready"
        SENT = "sent", "Sent"
        FAILED = "failed", "Failed"

    newsletter = models.ForeignKey(
        Newsletter,
        on_delete=models.CASCADE,
        related_name="digests",
    )
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    window_start = models.DateTimeField()
    window_end = models.DateTimeField()
    raw_sources = models.JSONField(default=list, blank=True)
    content_html = models.TextField(blank=True)
    content_text = models.TextField(blank=True)
    error = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Digest for {self.newsletter.name} — {self.window_end.date()}"
