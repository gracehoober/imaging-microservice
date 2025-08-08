from django.test import TestCase
from rest_framework import status
from django.urls import reverse


class TestImagingViewSet(TestCase):
    def setUp(self):
        super().setUp()
        self.list_url = reverse("imaging")
        self.detail_url = reverse(
            "imaging",
        )

    def test_retrieve_success(self):
        response = self.client.get(self.detail_url)
        assert response.status_code is status.HTTP_200_OK

    def test_list_success(self):
        response = self.client.get(self.list_url)
        assert response.status_code is status.HTTP_200_OK

    def test_create_success(self):
        image_payload = {}
        response = self.client.post(self.url, data=image_payload)
        assert response.status_code is status.HTTP_201_CREATED
