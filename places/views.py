from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Place


def index(request):
    places = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse('place_detail', args=[place.id])
                }
            }
        for place in Place.objects.all()]
    }

    return render(request, 'index.html', {'places': places})


def place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_info = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng
        }
    }
    return JsonResponse(place_info, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
