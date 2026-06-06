from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.first_name_input = "[data-test='firstName']"
        self.last_name_input = "[data-test='lastName']"
        self.zip_code_input = "[data-test='postalCode']"
        self.continue_button = "[data-test='continue']"
        self.finish_button = "[data-test='finish']"
        self.complete_header = ".complete-header"

    def fill_checkout_info(self, first_name, last_name, zip_code):
        self.fill_input(self.first_name_input, first_name)
        self.fill_input(self.last_name_input, last_name)
        self.fill_input(self.zip_code_input, zip_code)
        self.click_element(self.continue_button)

    def finish_purchase(self):
        self.click_element(self.finish_button)

    def get_completion_message(self):
        return self.page.locator(self.complete_header).inner_text()