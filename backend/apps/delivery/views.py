from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.newsletters.models import Newsletter


class TriggerDeliveryView(APIView):
    """Manually trigger a digest generation for a newsletter (owner only)."""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, newsletter_pk):
        try:
            newsletter = Newsletter.objects.get(pk=newsletter_pk, owner=request.user)
        except Newsletter.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        from .tasks import generate_digest

        task = generate_digest.delay(newsletter.id)
        return Response({"task_id": task.id}, status=status.HTTP_202_ACCEPTED)
