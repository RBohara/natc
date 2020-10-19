from django.db import models


class Membership(models.Model):
    title = models.CharField(
        max_length=150, default="Request for Membership Form", blank=True)
    filled_form = models.FileField(upload_to="docs/membership")

    def __str__(self):
        return self.title
