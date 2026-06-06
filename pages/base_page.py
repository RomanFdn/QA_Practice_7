from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def fill_input(self, selector: str, text: str):
        self.page.locator(selector).fill(text)

    def click_element(self, selector: str):
        self.page.locator(selector).click()