from django.shortcuts import render


from django.http import HttpResponse
from django.template import loader

from .models import Place


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
