from rest_framework_mongoengine import serializers

from . import models


class ProductSerializer(serializers.MongoEngineModelSerializer):
    class Meta:
        model = models.Product