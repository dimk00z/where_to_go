from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.template import loader

from .models import Place, Image


def place_detail_view(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    images_for_place = place.images.all()
    place_json = {
        'title': place.title,
        'imgs': [image.image.url for image in
                 images_for_place],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }
    return JsonResponse(place_json, json_dumps_params={'ensure_ascii': False, 'indent': 4})


def show_index_page(request):
    places_geo_json = {"type": "FeatureCollection",
                       "features": []}
    for place in Place.objects.all():
        places_geo_json["features"].append({
            "type": "Feature",
            "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.point_title,
                "placeId": place.id,
                "detailsUrl": place.get_absolute_url()
            }
        })

    return render(request, 'index.html', context={'places': places_geo_json})
