from . import models


class ProductFactory:

    def create_from_json_records(self, json_records):
        for json_record in json_records:
            self.create_from_json_record(json_record)

    def create_from_json_record(self, json_record):
        category_name = json_record['category']
        category, x = models.Category.objects.get_or_create(name=category_name)

        product = self._create(json_record)
        category.products.append(product)
        category.save()
        return product

    def _create(self, json_record):
        return models.Product.objects.create(
            name=json_record['name'],
            price=json_record['price'],
            promotion_price=json_record['promotion_price']
        )

