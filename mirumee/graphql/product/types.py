from graphene_django import DjangoObjectType

from ...product.models import Product
from ...product.models import ProductVariant

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"


class ProductVariantType(DjangoObjectType):
    class Meta:
        model = ProductVariant
        fields = "__all__"