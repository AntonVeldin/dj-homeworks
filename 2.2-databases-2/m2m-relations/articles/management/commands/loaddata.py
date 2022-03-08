import json

from django.core.management import BaseCommand

from articles.models import Article


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'path',
            nargs='*',
            type=str,
        )

    def handle(self, *args, **options):
        path = options['path']
        for each_path in path:
            with open(each_path, 'r', encoding='utf-8') as file:
                articles = json.load(file)
                for article in articles:
                    Article.objects.create(**article['fields'])

