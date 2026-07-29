from selenium.webdriver.common.by import By
from homework.homework_07.pages.base_page import BasePage


class CatalogPage(BasePage):
    DESKTOP_LOGO = (By.ID, "_desktop_logo")
    SEARCH_WIDGET = (By.ID, "search_widget")
    LEFT_COLUMN = (By.ID, "left-column")
    MAIN = (By.ID, "main")
    FOOTER = (By.ID, "footer")

    PRICE = (By.CLASS_NAME, "price")
    CURRENCY_BUTTON = (By.CSS_SELECTOR, "#_desktop_currency_selector button")
    USD_LINK = (By.LINK_TEXT, "USD $")

    def get_first_product_price(self):
        return self.find_element(CatalogPage.PRICE).text

    def switch_currency_to_usd(self):
        self.click(CatalogPage.CURRENCY_BUTTON)
        self.click(CatalogPage.USD_LINK)
