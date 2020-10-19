from django.db import models


class Event(models.Model):
    event_title = models.CharField(max_length=200)
    venue = models.CharField(max_length=500)
    organiser = models.CharField(max_length=100)
    time = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.event_title
