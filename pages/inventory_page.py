from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.title = ".title"
        self.add_backpack_btn = "[data-test='add-to-cart-sauce-labs-backpack']"
        self.remove_backpack_btn = "[data-test='remove-sauce-labs-backpack']"
        self.cart_badge = ".shopping_cart_badge"

    def add_backpack_to_cart(self):
        self.click_element(self.add_backpack_btn)

    def get_cart_badge_number(self):
        return self.page.locator(self.cart_badge).inner_text()