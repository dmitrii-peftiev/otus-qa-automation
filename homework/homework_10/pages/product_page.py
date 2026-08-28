import allure
from selenium.webdriver.common.by import By

from homework.homework_10.pages.base_page import BasePage


class ProductPage(BasePage):
    DESKTOP_LOGO = (By.ID, "_desktop_logo")
    SEARCH_WIDGET = (By.ID, "search_widget")
    PRODUCT_DESCRIPTION_SHORT_1 = (By.ID, "product-description-short-1")
    ADD_TO_CART_OR_REFRESH = (By.ID, "add-to-cart-or-refresh")
    FOOTER = (By.ID, "footer")

    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "add-to-cart")
    CART_MODAL = (By.ID, "blockcart-modal")

    @allure.step("Add product to cart")
    def add_to_cart(self):
        self.logger.info("Adding product to cart")
        self.click(self.ADD_TO_CART_BUTTON)

    @allure.step("Check that product page is open")
    def is_opened(self):
        self.logger.info("Checking that product page is open")
        assert self.find_element(self.PRODUCT_DESCRIPTION_SHORT_1)
        assert self.find_element(self.ADD_TO_CART_BUTTON)

    @allure.step("Check that cart modal is visible")
    def cart_is_visible(self):
        self.logger.info("Checking that cart modal is visible")
        assert self.find_element(self.CART_MODAL)
