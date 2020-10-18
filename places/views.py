from django.shortcuts import render, get_object_or_404


from django.http import HttpResponse
from django.template import loader

from .models import Place


def place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    return HttpResponse(place.title)


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
                "detailsUrl": "./static/places/moscow_legends.json"
            }
        })

    template = loader.get_template('index.html')
    context = {'places': places_geo_json}
    return HttpResponse(template.render(context, request))
