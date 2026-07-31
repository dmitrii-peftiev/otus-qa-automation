import random
from selenium.webdriver.common.by import By
from homework.homework_07.pages.base_page import BasePage


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

    def click_random_product(self):
        products = self.find_elements(self.PRODUCTS)
        random_product = random.choice(products)
        random_product.click()

    def get_first_product_price(self):
        return self.find_element(self.PRICE).text

    def switch_currency_to_usd(self):
        self.click(self.CURRENCY_BUTTON)
        self.click(self.USD_LINK)

    def is_opened(self):
        assert self.find_element(self.DESKTOP_LOGO)
        assert self.find_element(self.CAROUSEL)
        assert self.find_element(self.FOOTER)
