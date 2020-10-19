from django.db import models


class GalleryFile(models.Model):
    photo = models.ImageField(upload_to="photos/gallery", blank=True)
