import json
from decimal import Decimal


def test_products(db, client_query, product, product_second):
    products = [product, product_second]
    response = client_query(
        """
      query myproducts {
             products{
                price
                id
                name
                description
                quantity
            }
        }
        """
    )

    content = json.loads(response.content)
    product_response = content['data']['products']

    # Asserting by range of all responsed products
    for cp_index in range(0, len(product_response)):
        assert product_response[cp_index]['id'] == str(products[cp_index].id)
        assert product_response[cp_index]['description'] == products[cp_index].description
        assert product_response[cp_index]['quantity'] == products[cp_index].quantity
        assert product_response[cp_index]['price'] == str(products[cp_index].price)