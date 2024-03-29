from rest_framework_mongoengine import generics

from . import models
from . import serializers


class ProductAPIView(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        category = models.Category.objects.get(id=self.kwargs['category_id'])
        return category.products


class ProductDetailAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()


class CategoryAPIView(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()