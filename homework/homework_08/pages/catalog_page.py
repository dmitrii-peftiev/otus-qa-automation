import allure
from selenium.webdriver.common.by import By

from homework.homework_08.pages.base_page import BasePage


class CatalogPage(BasePage):
    DESKTOP_LOGO = (By.ID, "_desktop_logo")
    SEARCH_WIDGET = (By.ID, "search_widget")
    LEFT_COLUMN = (By.ID, "left-column")
    MAIN = (By.ID, "main")
    FOOTER = (By.ID, "footer")

    PRICE = (By.CLASS_NAME, "price")
    CURRENCY_BUTTON = (By.CSS_SELECTOR, "#_desktop_currency_selector button")
    USD_LINK = (By.LINK_TEXT, "USD $")

    @allure.step("Get first product price")
    def get_first_product_price(self):
        self.logger.info("Getting first product price from catalog")
        return self.find_element(self.PRICE).text

    @allure.step("Switch currency to USD")
    def switch_currency_to_usd(self):
        self.logger.info("Switching currency to USD")
        self.click(self.CURRENCY_BUTTON)
        self.click(self.USD_LINK)

    @allure.step("Check that catalog page is open")
    def is_opened(self):
        self.logger.info("Checking that catalog page is open")
        assert self.find_element(self.SEARCH_WIDGET)
        assert self.find_element(self.LEFT_COLUMN)
        assert self.find_element(self.MAIN)
        assert self.find_element(self.FOOTER)
