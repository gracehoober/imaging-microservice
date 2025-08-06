from django.urls import include, path

urlpatterns = [
    path("health/", include("imaging_service.health.urls")),
]
