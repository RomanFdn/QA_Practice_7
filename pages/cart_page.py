from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_button = "[data-test='checkout']"
        self.cart_item = ".cart_item"

    def click_checkout(self):
        self.click_element(self.checkout_button)
        
    def is_item_present(self):
        return self.page.locator(self.cart_item).is_visible()