import requests
from django.core.files.base import ContentFile
from django.core.management import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('place_json', type=str)

    def handle(self, *args, **options):
        self.stdout.write('Command execution')
        place_response = requests.get(options['place_json'])

        place_response.raise_for_status()

        place_data = place_response.json()
        place, place_created = Place.objects.get_or_create(
            title=place_data['title'],
            defaults={'point_title': place_data['title'],
                      'short_description': place_data['description_short'],
                      'long_description': place_data['description_long'],
                      'lng': place_data['coordinates']['lng'],
                      'lat': place_data['coordinates']['lat'],
                      },
        )

        if not place_created:
            self.stdout.write(self.style.WARNING(
                'The object has already been created'))
            return

        imgs_responses = [requests.get(img) for img in place_data['imgs']]

        for img_response in imgs_responses:
            if not img_response.ok:
                continue

            name = img_response.url.split('/')[-1]
            image = Image.objects.create(
                place=place,
            )
            image.image.save(name, ContentFile(
                img_response.content), save=True)

        self.stdout.write(self.style.SUCCESS(
            f'Successfully create place "{place}"'))
