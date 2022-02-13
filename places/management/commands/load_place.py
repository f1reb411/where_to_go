import os

import requests
from django.core.files.base import ContentFile
from django.core.management import BaseCommand

from places.models import Image, Place


class Command(BaseCommand):
    help = 'Load JSON data with place information from url to database'

    def add_arguments(self, parser):
        parser.add_argument('url')

    def handle(self, *args, **options):
        url = options['url']
        response = requests.get(url)
        response.raise_for_status()
        place_json = response.json()

        new_place, _ = Place.objects.get_or_create(
            title=place_json['title'],
            lng=place_json['coordinates']['lng'],
            lat=place_json['coordinates']['lat'],
            defaults={
                'description_short': place_json['description_short'],
                'description_long': place_json['description_long']
            }
        )

        for number, link in enumerate(place_json['imgs']):
            response = requests.get(link)
            response.raise_for_status()

            new_image, _ = Image.objects.get_or_create(
                place=new_place,
                position=number
            )

            new_image.image.save(
                os.path.basename(response.url), ContentFile(response.content)
            )
