from django.db import models


class Membership(models.Model):
    family_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    name1 = models.CharField(max_length=150, null=True, blank=True)
    name2 = models.CharField(max_length=150, null=True, blank=True)
    name3 = models.CharField(max_length=150, null=True, blank=True)
    relation1 = models.CharField(max_length=150, null=True, blank=True)
    relation2 = models.CharField(max_length=150, null=True, blank=True)
    relation3 = models.CharField(max_length=150, null=True, blank=True)
    unit = models.CharField(max_length=100)
    street_no = models.CharField(max_length=100)
    street_name = models.CharField(max_length=200)
    suburb = models.CharField(max_length=200)
    state = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=250)
    membership_type = models.CharField(max_length=30)
    receipt = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.family_name}"
