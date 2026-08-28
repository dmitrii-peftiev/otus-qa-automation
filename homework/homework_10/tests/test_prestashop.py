import allure
import pytest

from homework.homework_10.pages.admin_login_page import AdminLoginPage
from homework.homework_10.pages.catalog_page import CatalogPage
from homework.homework_10.pages.main_page import MainPage
from homework.homework_10.pages.product_page import ProductPage
from homework.homework_10.pages.registration_page import RegistrationPage

pytestmark = pytest.mark.homework_10


@allure.feature("Pages Availability")
@allure.story("Open standard pages")
class TestPagesAvailability:
    @allure.title("Check Main page availability")
    def test_main_page(self, browser):
        page = MainPage(browser)
        page.open()
        page.is_opened()

    @allure.title("Check Catalog page availability")
    def test_catalog_page(self, browser):
        page = CatalogPage(browser)
        page.open("/3-clothes")
        page.is_opened()

    @allure.title("Check Product page availability")
    def test_product_page(self, browser):
        page = ProductPage(browser)
        page.open("/men/1-2-hummingbird-printed-t-shirt.html")
        page.is_opened()

    @allure.title("Check Admin Login page availability")
    def test_admin_login_page(self, browser):
        page = AdminLoginPage(browser)
        page.open("/administration")
        page.is_opened()

    @allure.title("Check Registration page availability")
    def test_registration_page(self, browser):
        page = RegistrationPage(browser)
        page.open("/registration")
        page.is_opened()
