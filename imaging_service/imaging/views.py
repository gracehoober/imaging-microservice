from rest_framework.viewsets import ModelViewSet
from models import Images
from serializers import ImageSerializer


class ImagingViewSet(ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Images.objects.all()
