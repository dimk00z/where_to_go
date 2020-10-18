from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def show_index_page(request):
    places = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                        "coordinates": [37.63, 55.793676]
                },
                "properties": {
                    "title": "«Легенды Москвы",
                    "placeId": "moscow_legends",
                    "detailsUrl": "./static/places/moscow_legends.json"
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                        "coordinates": [37.65, 55.753676]
                },
                "properties": {
                    "title": "Крыши24.рф",
                    "placeId": "roofs24",
                    "detailsUrl": "./static/places/roofs24.json"
                }
            }
        ]
    }
    template = loader.get_template('index.html')
    context = {'places': places}
    return HttpResponse(template.render(context, request))
