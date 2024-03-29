import json

from django.core.urlresolvers import reverse

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


class ProductAPIViewTests(MongoTestCase):
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
        self.factory.create_from_json_records(self.records)
        category = models.Category.objects.get(name='artykuły biurowe')
        self.url = reverse('product_list', args=[category.id])
        self.response = self.client.get(self.url)

    def test_status_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_record_count(self):
        data = json.loads(self.response.content.decode('utf-8'))
        self.assertEqual(2, len(data))


class ProductDetailAPIViewTests(MongoTestCase):
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
        self.factory.create_from_json_records(self.records)
        self.product = models.Product.objects.first()
        self.url = reverse('product_detail', args=[self.product.id])
        self.response = self.client.get(self.url)

    def test_status_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_record_detail(self):
        record = json.loads(self.response.content.decode('utf-8'))
        self.assertEqual(self.product.name, record['name'])
        self.assertEqual(str(self.product.price), record['price'])
        self.assertEqual(str(self.product.promotion_price),
                         record['promotion_price'])


class CategoryAPIViewTests(MongoTestCase):
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
        self.factory.create_from_json_records(self.records)
        self.url = reverse('category_list')
        self.response = self.client.get(self.url)
        self.categories_data = json.loads(self.response.content.decode('utf-8'))

    def test_status_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_count(self):
        self.assertEqual(2, len(self.categories_data))

    def test_product_count(self):
        self.assertEqual(2, self.categories_data[0]['product_count'])
        self.assertEqual(1, self.categories_data[1]['product_count'])