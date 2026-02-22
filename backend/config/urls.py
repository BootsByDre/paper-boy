from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("apps.users.urls", namespace="users")),
    path("api/v1/", include("apps.newsletters.urls", namespace="newsletters")),
    path("api/v1/", include("apps.delivery.urls", namespace="delivery")),
]
