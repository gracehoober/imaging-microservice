import boto3
from botocore.exceptions import ClientError
from settings import IMAGE_SERVICE_BUCKET
from rest_framework.response import Response
from rest_framework import status


class S3BucketAdaptor:
    def __init__(self):
        self.s3 = boto3.client("s3")
        self.bucket = self.s3.Bucket(IMAGE_SERVICE_BUCKET)

    def upload_image(self, image, modality):
        """Uploads a image to the designated s3 bucket.
        Returns a presigned url for the image.
        """
        expiration = None
        try:
            response = self.s3.generate_presigned_url(
                image,
                Params={"Bucket": self.bucket, "Key": modality},
                ExpiresIn=expiration,
            )
        except ClientError as e:
            data = {"error": e}
            return Response(data, status.HTTP_424_FAILED_DEPENDENCY)

        return response
