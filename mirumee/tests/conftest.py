import pytest
from graphene_django.utils.testing import graphql_query
from ..product.models import Product
from decimal import Decimal


@pytest.fixture
def client_query(client):
    def func(*args, **kwargs):
        return graphql_query(*args, **kwargs, client=client)

    return func


@pytest.fixture
def product():
    product = Product.objects.create(
        name="Test Product",
        description="Product description",
        price=Decimal("10.00"),
        quantity=10.00
    )

    return product


@pytest.fixture
def product_second():
    product = Product.objects.create(
        name="Test product 2",
        description="Product test2",
        price=Decimal("20.00"),
        quantity=20.00
    )

    return product
