from rest_framework import serializers

from .models import Digest, Newsletter


class NewsletterSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Newsletter
        fields = [
            "id",
            "owner",
            "name",
            "topic",
            "cadence",
            "is_active",
            "last_delivered_at",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "last_delivered_at", "created_at", "updated_at"]


class DigestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Digest
        fields = [
            "id",
            "newsletter",
            "status",
            "window_start",
            "window_end",
            "content_html",
            "content_text",
            "created_at",
            "sent_at",
        ]
        read_only_fields = fields
