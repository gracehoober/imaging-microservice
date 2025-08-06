from django.test import TestCase
from rest_framework import status
from django.urls import reverse


class TestHealthView(TestCase):
    def setUp(self):
        self.url = reverse("health")

    def test_get_view_success(self):
        response = self.client.get(self.url)
        assert response.status_code is status.HTTP_200_OK
        data = response.json()["data"]
        assert data == "Imaging Service App is healthy!"


# all other HTTP methods should return default message that not allowed
