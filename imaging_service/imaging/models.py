from django.db import models


class Images(models.Model):
    MODALITY_CHOICES = (
        ("CT", "Computed Tomography"),
        ("CTA", "Computed Tomography Angiography"),
        ("XR", "X-ray"),
        ("MRI", "Magnetic Resonance Imaging"),
    )

    id = models.UUIDField(null=False)
    url = models.URLField(null=False)
    modality = models.CharField(max_length=50, choices=MODALITY_CHOICES, blank=False)
    patient_id = models.UUIDField(null=False)
