import allure
import pytest

from homework.homework_10.pages.admin_login_page import AdminLoginPage
from homework.homework_10.pages.catalog_page import CatalogPage
from homework.homework_10.pages.main_page import MainPage
from homework.homework_10.pages.product_page import ProductPage

pytestmark = pytest.mark.homework_10

ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "Admin123!"


@allure.feature("Admin Actions")
@allure.story("Login and Logout")
@allure.title("Success admin login and logout cycle")
def test_admin_login_logout(browser):
    page = AdminLoginPage(browser)
    page.open("/administration")

    page.login(ADMIN_EMAIL, ADMIN_PASSWORD)
    page.dashboard_is_opened()

    page.logout()
    page.is_opened()


@allure.feature("Cart and Shopping")
@allure.story("Add to cart")
@allure.title("Add random product to cart from Main page")
def test_add_random_product_to_cart(browser):
    main_page = MainPage(browser)
    main_page.open()

    main_page.click_random_product()

    product_page = ProductPage(browser)
    product_page.add_to_cart()
    product_page.cart_is_visible()


@allure.feature("Currency Options")
@allure.story("Switch currency")
@allure.title("Check currency change on Main page")
def test_currency_switch_on_main_page(browser):
    page = MainPage(browser)
    page.open()

    initial_price = page.get_first_product_price()
    page.switch_currency_to_usd()
    new_price = page.get_first_product_price()

    with allure.step("Check that text price is different"):
        assert initial_price != new_price


@allure.feature("Currency Options")
@allure.story("Switch currency")
@allure.title("Check currency change on Catalog page")
def test_currency_switch_in_catalog(browser):
    page = CatalogPage(browser)
    page.open("/3-clothes")

    initial_price = page.get_first_product_price()
    page.switch_currency_to_usd()
    new_price = page.get_first_product_price()

    with allure.step("Check that text price is different"):
        assert initial_price != new_price
