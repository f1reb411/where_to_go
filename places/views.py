from django.shortcuts import render

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
                    "detailsUrl": 'places/moscow_legends.json'
                }
            }
        for place in Place.objects.all()]
    }

    return render(request, 'index.html', {'places': places})
