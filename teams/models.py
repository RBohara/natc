from django.db import models

# Create your models here.


class Team(models.Model):

    CATEGORY = (
        ('Executive Committee', 'Executive Committee'),
        ('Advisors', 'Advisors'),
        ('Members', 'Members'),
    )

    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=25, choices=CATEGORY)

    def __str__(self):
        return self.name
