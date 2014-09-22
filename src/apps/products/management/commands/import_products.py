import json

from django.core.management import BaseCommand

from ...factories import ProductFactory


class Command(BaseCommand):

    def handle(self, file_name, **options):
        with open(file_name) as document:
            shop_data = json.load(document)
        product_factory = ProductFactory()
        product_factory.create_from_json_records(shop_data['products'])
