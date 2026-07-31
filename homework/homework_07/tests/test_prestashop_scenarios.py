import pytest
from homework.homework_07.pages.main_page import MainPage
from homework.homework_07.pages.catalog_page import CatalogPage
from homework.homework_07.pages.product_page import ProductPage
from homework.homework_07.pages.admin_login_page import AdminLoginPage

pytestmark = pytest.mark.homework_07

ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "Admin123!"


def test_admin_login_logout(browser):
    page = AdminLoginPage(browser)
    page.open("/administration")

    page.login(ADMIN_EMAIL, ADMIN_PASSWORD)
    page.dashboard_is_opened()

    page.logout()
    page.is_opened()


def test_add_random_product_to_cart(browser):
    main_page = MainPage(browser)
    main_page.open()

    main_page.click_random_product()

    product_page = ProductPage(browser)
    product_page.add_to_cart()
    product_page.cart_is_visible()


def test_currency_switch_on_main_page(browser):
    page = MainPage(browser)
    page.open()

    initial_price = page.get_first_product_price()
    page.switch_currency_to_usd()
    new_price = page.get_first_product_price()

    assert initial_price != new_price


def test_currency_switch_in_catalog(browser):
    page = CatalogPage(browser)
    page.open("/3-clothes")

    initial_price = page.get_first_product_price()
    page.switch_currency_to_usd()
    new_price = page.get_first_product_price()

    assert initial_price != new_price
