from rest_framework.views import APIView
from rest_framework.response import Response


class HealthView(APIView):
    def get(self, request):
        data = {"data": "Imaging Service App is healthy!"}
        return Response(data=data, status=200)
