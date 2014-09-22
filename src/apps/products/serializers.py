from rest_framework import serializers as base_serializers
from rest_framework_mongoengine import serializers

from . import models


class ProductSerializer(serializers.MongoEngineModelSerializer):
    class Meta:
        model = models.Product


class CategorySerializer(serializers.MongoEngineModelSerializer):
    product_count = base_serializers.Field(source='product_count')

    class Meta:
        model = models.Category
        fields = ['id', 'name', 'product_count']