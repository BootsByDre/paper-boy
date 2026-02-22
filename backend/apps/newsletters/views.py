from rest_framework import generics, permissions

from .models import Digest, Newsletter
from .serializers import DigestSerializer, NewsletterSerializer


class NewsletterListCreateView(generics.ListCreateAPIView):
    serializer_class = NewsletterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Newsletter.objects.filter(owner=self.request.user)


class NewsletterDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsletterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Newsletter.objects.filter(owner=self.request.user)


class DigestListView(generics.ListAPIView):
    serializer_class = DigestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Digest.objects.filter(
            newsletter__owner=self.request.user,
            newsletter_id=self.kwargs["newsletter_pk"],
        )


class DigestDetailView(generics.RetrieveAPIView):
    serializer_class = DigestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Digest.objects.filter(newsletter__owner=self.request.user)
