from rest_framework.serializers import ModelSerializer, ImageField
from models import Images
from adaptors.S3_bucket_adaptor import S3BucketAdaptor


class ImageSerializer(ModelSerializer):
    image = ImageField(max_length=None, use_url=True)

    class Meta:
        model = Images
        fields = ["id", "url", "modality"]
        read_only_fields = ["patient_id"]

    def create(self, validated_data):
        image_url = self._upload_image(validated_data)
        validated_data["url"] = image_url
        instance = Images.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        pass

    def _upload_image(self, validated_data):
        image = validated_data.get("image")
        modality = validated_data.get("modality")
        image_url = S3BucketAdaptor().upload_image(image=image, modality=modality)
        return image_url
