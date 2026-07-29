from selenium.webdriver.common.by import By
from homework.homework_07.pages.base_page import BasePage


class ProductPage(BasePage):
    DESKTOP_LOGO = (By.ID, "_desktop_logo")
    SEARCH_WIDGET = (By.ID, "search_widget")
    PRODUCT_DESCRIPTION_SHORT_1 = (By.ID, "product-description-short-1")
    ADD_TO_CART_OR_REFRESH = (By.ID, "add-to-cart-or-refresh")
    FOOTER = (By.ID, "footer")

    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "add-to-cart")
    CART_MODAL = (By.ID, "blockcart-modal")

    def add_to_cart(self):
        self.click(ProductPage.ADD_TO_CART_BUTTON)
