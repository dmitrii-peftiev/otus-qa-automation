import random

import allure
from selenium.webdriver.common.by import By

from homework.homework_10.pages.base_page import BasePage


class MainPage(BasePage):
    DESKTOP_LOGO = (By.ID, "_desktop_logo")
    SEARCH_WIDGET = (By.ID, "search_widget")
    CAROUSEL = (By.ID, "carousel")
    CUSTOM_TEXT = (By.ID, "custom-text")
    FOOTER = (By.ID, "footer")

    PRODUCTS = (By.CLASS_NAME, "thumbnail-top")
    PRICE = (By.CLASS_NAME, "price")
    CURRENCY_BUTTON = (By.CSS_SELECTOR, "#_desktop_currency_selector button")
    USD_LINK = (By.LINK_TEXT, "USD $")

    @allure.step("Click random product")
    def click_random_product(self):
        self.logger.info("Selecting and clicking random product")
        products = self.find_elements(self.PRODUCTS)
        random_product = random.choice(products)
        random_product.click()

    @allure.step("Get first product price")
    def get_first_product_price(self):
        self.logger.info("Getting first product price from main page")
        return self.find_element(self.PRICE).text

    @allure.step("Switch currency to USD")
    def switch_currency_to_usd(self):
        self.logger.info("Switching currency to USD")
        self.click(self.CURRENCY_BUTTON)
        self.click(self.USD_LINK)

    @allure.step("Check that main page is open")
    def is_opened(self):
        self.logger.info("Checking that main page is open")
        assert self.find_element(self.DESKTOP_LOGO)
        assert self.find_element(self.CAROUSEL)
        assert self.find_element(self.FOOTER)
