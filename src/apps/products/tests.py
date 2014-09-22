from commons.testing import MongoTestCase

from . import factories
from . import models


class ProductFactoryTests(MongoTestCase):
    records = [
        {
            'name': 'długopis',
            'price': 3,
            'promotion_price': 1,
            'category': 'artykuły biurowe'
        },
        {
            'name': 'ołówek',
            'price': 2,
            'promotion_price': 1,
            'category': 'artykuły biurowe'
        },
        {
            'name': 'tulipan',
            'price': 3,
            'promotion_price': 1,
            'category': 'kwiaty cięte'
        }
    ]

    def setUp(self):
        self.factory = factories.ProductFactory()

    def test_create_1_product(self):
        self.factory.create_from_json_record(self.records[0])
        self.assertEqual(models.Product.objects.count(), 1)

    def test_create_3_products(self):
        self.factory.create_from_json_records(self.records)
        self.assertEqual(models.Product.objects.count(), 3)

    def test_product_detail_after_create(self):
        product = self.factory.create_from_json_record(self.records[0])
        self.assertEqual(self.records[0]['name'], product.name)
        self.assertEqual(self.records[0]['price'], product.price)
        self.assertEqual(self.records[0]['promotion_price'],
                         product.promotion_price)

    def test_create_1_category(self):
        self.factory.create_from_json_record(self.records[0])
        self.assertEqual(models.Category.objects.count(), 1)

    def test_create_1_category_for_many_products_with_same_category(self):
        self.factory.create_from_json_records(self.records[:2])
        self.assertEqual(models.Category.objects.count(), 1)

    def test_create_2_category_for_product_with_different_category(self):
        self.factory.create_from_json_records(self.records)
        self.assertEqual(models.Category.objects.count(), 2)
