from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=100)
    description_short = models.TextField(blank=True)
    description_long = models.TextField(blank=True)
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title
