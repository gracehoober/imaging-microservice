from django.urls import path
from imaging_service.health.views import HealthView


urlpatterns = [
    path("", HealthView.as_view(), name="health"),
]
