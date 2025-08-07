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

    def test_post_returns_valid_response(self):
        response = self.client.post(self.url, data={"data": "Change this"})
        assert response.status_code is status.HTTP_405_METHOD_NOT_ALLOWED

    def test_put_returns_valid_response(self):
        response = self.client.put(self.url, data={"data": "Change this"})
        assert response.status_code is status.HTTP_405_METHOD_NOT_ALLOWED

    def test_patch_returns_valid_response(self):
        response = self.client.patch(self.url, data={"data": "Change this"})
        assert response.status_code is status.HTTP_405_METHOD_NOT_ALLOWED

    def test_delete_returns_valid_response(self):
        response = self.client.delete(self.url, data={"data": "Change this"})
        assert response.status_code is status.HTTP_405_METHOD_NOT_ALLOWED
