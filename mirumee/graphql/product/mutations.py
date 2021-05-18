import graphene
from .types import ProductType, ProductVariantType
from ...product.models import Product, ProductVariant


class ProductCrateInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    price = graphene.Decimal(required=True)
    description = graphene.String(required=True)
    quantity = graphene.Int()


class ProductVariantCreateInput(graphene.InputObjectType):
    product = graphene.String(required=True)
    name = graphene.String(required=True)
    sku = graphene.String(required=True)
    price = graphene.Decimal(required=True)


class ProductCreate(graphene.Mutation):
    product = graphene.Field(ProductType)

    class Arguments:
        input = ProductCrateInput(required=True)

    def clean_input(self, input):
        return input

    def mutate(self, root, _info, input):
        cleaned_input = self.clean_input(input)

        product = Product.objects.create(**cleaned_input)

        return ProductCreate(product=product)


class ProductVariantCreate(graphene.Mutation):
    product_variant = graphene.Field(ProductVariantType)

    class Arguments:
        input = ProductVariantCreateInput

    def clean_input(self, input):
        return input

    def mutate(self, root, _info, input):
        cleaned_input = self.clean_input(input)

        product_variant = ProductVariant.objects.create(**cleaned_input)

        return ProductVariantCreate(product_variant=product_variant)