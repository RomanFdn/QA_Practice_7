from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import get_config
from utils.logger import log

config = get_config()

def test_positive_login(setup):
    page = setup
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    
    log.info("Запуск тесту: Позитивний логін")
    login_page.navigate(config["base_url"])
    login_page.login("standard_user", "secret_sauce")
    
    assert page.locator(inventory_page.title).is_visible()

def test_negative_login(setup):
    page = setup
    login_page = LoginPage(page)
    
    log.info("Запуск тесту: Негативний логін")
    login_page.navigate(config["base_url"])
    login_page.login("standard_user", "wrong_password")
    
    assert "Username and password do not match" in login_page.get_error_text()

def test_add_to_cart(setup):
    page = setup
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    
    log.info("Запуск тесту: Додавання товару")
    login_page.navigate(config["base_url"])
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page.add_backpack_to_cart()
    assert inventory_page.get_cart_badge_number() == "1"