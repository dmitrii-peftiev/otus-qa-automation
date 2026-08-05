import allure
from selenium.webdriver.common.by import By

from homework.homework_08.pages.base_page import BasePage


class RegistrationPage(BasePage):
    DESKTOP_LOGO = (By.ID, "_desktop_logo")
    SEARCH_WIDGET = (By.ID, "search_widget")
    FIELD_EMAIL = (By.ID, "field-email")
    FIELD_PASSWORD = (By.ID, "field-password")
    FOOTER = (By.ID, "footer")

    @allure.step("Check that registration page is open")
    def is_opened(self):
        self.logger.info("Checking that registration page is open")
        assert self.find_element(self.FIELD_EMAIL)
        assert self.find_element(self.FIELD_PASSWORD)
