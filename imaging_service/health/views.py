from rest_framework.views import APIView
from rest_framework.response import Response


class HealthView(APIView):
    http_method_names = ["get"]

    def get(self):
        data = {"data": "Imaging Serice App is healthy!"}
        return Response(data=data, status=200)
