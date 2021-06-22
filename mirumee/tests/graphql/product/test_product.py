import json



def test_product_by_id(db, client_query, product):

    response = client_query(
        """
        query myproduct($id: ID!) {
            product(id: $id){
                price
                id
                name
                description
                quantity
            }
        }
        """,
        variables={'id':1}
    )
    content = json.loads(response.content)


    product_response = content['data']['product']

    assert product_response['id'] == str(product.id)
    assert product_response['description'] == product.description
    assert product_response['quantity'] == product.quantity
    assert product_response['price'] == str(product.price)
'''

def test_products_list(db, product, product_second):
    response = product, product_second(
        """
        query Products(){
            product(){
            id
            name
            description
            price
            quantity
        }
            
        """

    )
    content = json.loads(response.content)

    product_list_response = content['data']['product']['product_second']

    assert product_list_response['id'] == str(product.id)
    assert product_list_response['description'] == product.description
    assert product_list_response['quantity'] == product.quantity
    assert product_list_response['price'] == str(product.price)

    assert product_list_response['id'] == str(product_second.id)
    assert product_list_response['description'] == product_second.description
    assert product_list_response['quantity'] == product_second.quantity
    assert product_list_response['price'] == str(product_second.price)'''