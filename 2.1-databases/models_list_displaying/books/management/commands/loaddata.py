from books.models import Book
import json

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'path',
            nargs='*',
            type=str
        )

    def handle(self, *args, **options):
        path = options['path']
        for each_path in path:
            with open(each_path, 'r', encoding="utf-8") as file:
                books = json.load(file)
            for each_book in books:
                book = Book(
                    name=each_book['fields']['name'],
                    author=each_book['fields']['author'],
                    pub_date=each_book['fields']['pub_date']
                )
                book.save()

