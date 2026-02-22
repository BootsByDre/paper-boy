from django.urls import path

from . import views

app_name = "newsletters"

urlpatterns = [
    path("newsletters/", views.NewsletterListCreateView.as_view(), name="list"),
    path("newsletters/<int:pk>/", views.NewsletterDetailView.as_view(), name="detail"),
    path(
        "newsletters/<int:newsletter_pk>/digests/",
        views.DigestListView.as_view(),
        name="digest-list",
    ),
    path("digests/<int:pk>/", views.DigestDetailView.as_view(), name="digest-detail"),
]
