from django.urls import path

from . import views

app_name = "delivery"

urlpatterns = [
    path(
        "newsletters/<int:newsletter_pk>/trigger/",
        views.TriggerDeliveryView.as_view(),
        name="trigger",
    ),
]
