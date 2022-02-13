from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('название', max_length=100)
    description_short = models.TextField('короткое описание', blank=True)
    description_long = HTMLField('длинное описание', blank=True)
    lng = models.FloatField('долгота')
    lat = models.FloatField('широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField('картинка')
    position = models.PositiveIntegerField(default=0, verbose_name='позиция')

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.id} {self.place}'
