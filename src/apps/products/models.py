import mongoengine


class Product(mongoengine.Document):
    name = mongoengine.StringField()
    price = mongoengine.DecimalField()
    promotion_price = mongoengine.DecimalField()


class Category(mongoengine.Document):
    name = mongoengine.StringField()
    products = mongoengine.ListField(mongoengine.ReferenceField(Product))