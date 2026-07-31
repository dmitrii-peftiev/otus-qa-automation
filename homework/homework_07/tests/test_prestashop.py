import pytest
from homework.homework_07.pages.main_page import MainPage
from homework.homework_07.pages.catalog_page import CatalogPage
from homework.homework_07.pages.product_page import ProductPage
from homework.homework_07.pages.admin_login_page import AdminLoginPage
from homework.homework_07.pages.registration_page import RegistrationPage

pytestmark = pytest.mark.homework_07


def test_main_page(browser):
    page = MainPage(browser)
    page.open()
    page.is_opened()


def test_catalog_page(browser):
    page = CatalogPage(browser)
    page.open("/3-clothes")
    page.is_opened()


def test_product_page(browser):
    page = ProductPage(browser)
    page.open("/men/1-2-hummingbird-printed-t-shirt.html")
    page.is_opened()


def test_admin_login_page(browser):
    page = AdminLoginPage(browser)
    page.open("/administration")
    page.is_opened()


def test_registration_page(browser):
    page = RegistrationPage(browser)
    page.open("/registration")
    page.is_opened()
