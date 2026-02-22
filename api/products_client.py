import requests

class ProductsClient:

    BASE_URL = "https://dummyjson.com"

    # -----------------------------------
    # GET all products
    # -----------------------------------
    def get_all_products(self):
        response = requests.get(f"{self.BASE_URL}/products")
        return response

    # -----------------------------------
    # GET product by ID
    # -----------------------------------
    def get_product_by_id(self, product_id):
        response = requests.get(
            f"{self.BASE_URL}/products/{product_id}"
        )
        return response