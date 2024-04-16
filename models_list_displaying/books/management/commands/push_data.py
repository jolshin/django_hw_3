import json

from django.core.management.base import BaseCommand
from books.models import Book
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('fixtures/books.json', 'r') as file:
            books = json.load(file)

        for book in books:
            record = Book(
                name = book['fields']['name'],
                author = book['fields']['author'],
                pub_date = book['fields']['pub_date'],
            )
            record.slug = slugify(record.pub_date)
            record.save()
