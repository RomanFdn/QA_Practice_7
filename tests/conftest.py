import pytest
from playwright.sync_api import sync_playwright
from config.config import get_config
from utils.logger import log

def pytest_addoption(parser):
    """Додаємо власні параметри командного рядка для pytest."""
    parser.addoption("--browser_type", action="store", default="chromium", help="chromium, firefox, webkit")
    parser.addoption("--device_type", action="store", default="desktop", help="desktop, tablet, mobile")

@pytest.fixture(scope="session")
def setup(request):
    log.info("Ініціалізація мультибраузерного тестового середовища...")
    config = get_config()
    
    browser_param = request.config.getoption("--browser_type")
    device_param = request.config.getoption("--device_type")
    
    with sync_playwright() as p:
        if browser_param == "firefox":
            browser_engine = p.firefox
        elif browser_param == "webkit":
            browser_engine = p.webkit
        else:
            browser_engine = p.chromium

        browser = browser_engine.launch(headless=config["headless"], slow_mo=200)
        
        if device_param == "mobile":
            device_config = p.devices["iPhone 14"]
            log.info(f"Запуск на {browser_param} з емуляцією Мобільного пристрою (iPhone 14)")
        elif device_param == "tablet":
            device_config = p.devices["iPad Mini"]
            log.info(f"Запуск на {browser_param} з емуляцією Планшета (iPad Mini)")
        else:
            device_config = {
                "viewport": {"width": 1920, "height": 1080},
                "has_touch": False
            }
            log.info(f"Запуск на {browser_param} у режимі Настільного ПК (1920x1080)")

        context = browser.new_context(**device_config)
        page = context.new_page()
        
        yield page
        
        browser.close()
        log.info("Мультибраузерна сесія успішно завершена.")
import pytest
from datetime import datetime

def pytest_configure(config):
    from pytest_metadata.plugin import metadata_key
    
    config.stash[metadata_key]["Назва проєкту"] = "QA Automation Framework"
    config.stash[metadata_key]["Модуль"] = "Системне (E2E) тестування"
    config.stash[metadata_key]["Час запуску"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    config.stash[metadata_key]["Фреймворк"] = "Playwright & Pytest"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    
    extras = getattr(report, "extras", [])

    if report.when == "call":
        extras.append(pytest_html.extras.url("https://www.saucedemo.com/"))
        
        if report.failed:
            page = item.funcargs.get("page", None)
            if not page:
                page = item.funcargs.get("setup", None)
            
            if page:
                import os
                if not os.path.exists("screenshots"):
                    os.makedirs("screenshots")
                    
                screenshot_path = f"screenshots/{item.name}.png"
                page.screenshot(path=screenshot_path)
                extras.append(pytest_html.extras.image(screenshot_path))
        
        report.extras = extras