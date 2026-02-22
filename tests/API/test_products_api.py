import allure

from api.products_client import ProductsClient

@allure.feature("Api Validations")
@allure.story("GET /products endpoint validations")
@allure.severity(allure.severity_level.NORMAL)
def test_get_all_products():

    client = ProductsClient()

    response = client.get_all_products()

    assert response.status_code == 200

    body = response.json()

    # Validate products list
    assert "products" in body
    assert isinstance(body["products"], list)

    product = body["products"][0]

    assert isinstance(product["id"], int)
    assert isinstance(product["title"], str)
    assert isinstance(product["price"], (int, float))


@allure.feature("Api Validations")
@allure.story("GET /products/{id} endpoint validations")
@allure.severity(allure.severity_level.NORMAL)
def test_get_single_product():

    client = ProductsClient()

    product_id = 1

    response = client.get_product_by_id(product_id)

    assert response.status_code == 200

    product = response.json()

    assert product["id"] == product_id
    assert isinstance(product["id"], int)
    assert isinstance(product["title"], str)
    assert isinstance(product["price"], (int, float))


@allure.feature("Api Validations")
@allure.story("GET product with invalid ID")
@allure.severity(allure.severity_level.NORMAL)
def test_get_product_invalid_id():

    client = ProductsClient()

    invalid_id = 999999

    response = client.get_product_by_id(invalid_id)

    assert response.status_code == 404

    body = response.json()

    assert "message" in body
    assert isinstance(body["message"], str)