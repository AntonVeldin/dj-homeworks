from slugify import slugify
import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for each_phone in phones:
            phone = Phone(
                name=each_phone['name'],
                price=each_phone['price'],
                image=each_phone['image'],
                release_date=each_phone['release_date'],
                lte_exists=each_phone['lte_exists'],
                slug=slugify(each_phone['name'])
            )
            phone.save()

