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

    assert page.find_element(MainPage.DESKTOP_LOGO)
    assert page.find_element(MainPage.SEARCH_WIDGET)
    assert page.find_element(MainPage.CAROUSEL)
    assert page.find_element(MainPage.CUSTOM_TEXT)
    assert page.find_element(MainPage.FOOTER)


def test_catalog_page(browser):
    page = CatalogPage(browser)
    page.open("/3-clothes")

    assert page.find_element(CatalogPage.DESKTOP_LOGO)
    assert page.find_element(CatalogPage.SEARCH_WIDGET)
    assert page.find_element(CatalogPage.LEFT_COLUMN)
    assert page.find_element(CatalogPage.MAIN)
    assert page.find_element(CatalogPage.FOOTER)


def test_product_page(browser):
    page = ProductPage(browser)
    page.open("/men/1-2-hummingbird-printed-t-shirt.html")

    assert page.find_element(ProductPage.DESKTOP_LOGO)
    assert page.find_element(ProductPage.SEARCH_WIDGET)
    assert page.find_element(ProductPage.PRODUCT_DESCRIPTION_SHORT_1)
    assert page.find_element(ProductPage.ADD_TO_CART_OR_REFRESH)
    assert page.find_element(ProductPage.FOOTER)


def test_admin_login_page(browser):
    page = AdminLoginPage(browser)
    page.open("/administration")

    assert page.find_element(AdminLoginPage.EMAIL)
    assert page.find_element(AdminLoginPage.PASSWD)
    assert page.find_element(AdminLoginPage.SUBMIT_LOGIN)
    assert page.find_element(AdminLoginPage.STAY_LOGGED_IN)
    assert page.find_element(AdminLoginPage.FORGOT_PASSWORD_LINK)


def test_registration_page(browser):
    page = RegistrationPage(browser)
    page.open("/registration")

    assert page.find_element(RegistrationPage.DESKTOP_LOGO)
    assert page.find_element(RegistrationPage.SEARCH_WIDGET)
    assert page.find_element(RegistrationPage.FIELD_EMAIL)
    assert page.find_element(RegistrationPage.FIELD_PASSWORD)
    assert page.find_element(RegistrationPage.FOOTER)
