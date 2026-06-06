from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.config import get_config
import pytest

config = get_config()

def test_end_to_end_purchase_scenario(setup):

    page = setup
    
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.navigate(config["base_url"])
    login_page.login("standard_user", "secret_sauce")
    assert page.locator(inventory_page.title).is_visible(), "Не вдалося увійти в систему"

    inventory_page.add_backpack_to_cart()
    assert inventory_page.get_cart_badge_number() == "1", "Товар не додався у кошик"
    inventory_page.go_to_cart()

    assert cart_page.is_item_present(), "Кошик порожній"
    cart_page.click_checkout()

    checkout_page.fill_checkout_info("Ivan", "Bebra", "79000")

    checkout_page.finish_purchase()

    assert checkout_page.get_completion_message() == "Thank you for your order!", "Покупка не завершена"