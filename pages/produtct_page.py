from playwright.sync_api import Page


class ProductPage:

    def __init__(self, page: Page):
        self.page = page

        # Products page title
        self.products_title = page.locator(".title")

        # Inventory items
        self.inventory_items = page.locator(".inventory_item")

        # Add to cart buttons
        self.add_to_cart_buttons = page.locator("button.btn_inventory")

        # Shopping cart icon
        self.cart_icon = page.locator(".shopping_cart_link")

        #Product List
        self.product_list = page.locator(".inventory_item")

         # Cart badge count
        self.cart_badge = page.locator(".shopping_cart_badge")

        self.product_names = page.locator(".inventory_item_name")

    # ---------- Validations ----------

    def is_products_page_displayed(self):
        return self.products_title.is_visible()
    
    def is_logged_in(self):
        return self.products_title.is_visible()

    def get_products_count(self):
        return self.inventory_items.count()
    
    def get_product_list(self):
        return self.product_list.all()
    


    # ---------- Actions ----------

    def add_first_product_to_cart(self):
        self.add_to_cart_buttons.first.click()

    def add_product_to_cart_by_index(self, index: int):
        self.add_to_cart_buttons.nth(index).click()

    def open_cart(self):
        self.cart_icon.click()

    def add_product_to_cart(self, product_name: str):

        product = self.page.locator(
            ".inventory_item",
            has=self.page.locator(
                ".inventory_item_name",
                has_text=product_name
            )
        )
        product.locator("button").click()

    def get_cart_count(self):

        if self.cart_badge.is_visible():
            return int(self.cart_badge.text_content().strip())

        return 0
    
    def add_multiple_products_to_cart(self, product_names: list):
        for product_name in product_names:
            self.add_product_to_cart(product_name)