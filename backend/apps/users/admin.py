from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ["email", "username", "timezone", "is_active", "date_joined"]
    list_filter = ["is_active", "is_staff"]
    search_fields = ["email", "username"]
    ordering = ["-date_joined"]
    fieldsets = UserAdmin.fieldsets + (
        ("Profile", {"fields": ("timezone",)}),
    )
