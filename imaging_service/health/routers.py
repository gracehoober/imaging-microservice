from rest_framework import routers

from health.views import HealthView

router = routers.SimpleRouter()
router.register(r"", HealthView, basename="health")
