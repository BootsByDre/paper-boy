from django.contrib import admin

from .models import Digest, Newsletter


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ["name", "owner", "cadence", "is_active", "last_delivered_at", "created_at"]
    list_filter = ["cadence", "is_active"]
    search_fields = ["name", "owner__email", "topic"]
    raw_id_fields = ["owner"]


@admin.register(Digest)
class DigestAdmin(admin.ModelAdmin):
    list_display = ["newsletter", "status", "window_start", "window_end", "sent_at"]
    list_filter = ["status"]
    search_fields = ["newsletter__name"]
    raw_id_fields = ["newsletter"]
