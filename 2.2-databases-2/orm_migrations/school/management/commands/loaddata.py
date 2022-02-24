from django.core.management import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('school.json', 'r') as file:
            pass
        pass
