import pytest
from playwright.sync_api import sync_playwright
from config.config import get_config
from utils.logger import log

@pytest.fixture(scope="session")
def setup():
    log.info("Ініціалізація тестового середовища...")
    config = get_config()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=config["headless"], slow_mo=300)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()
        log.info("Завершення тестування.")