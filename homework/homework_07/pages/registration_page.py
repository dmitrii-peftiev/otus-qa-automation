from selenium.webdriver.common.by import By
from homework.homework_07.pages.base_page import BasePage


class RegistrationPage(BasePage):
    DESKTOP_LOGO = (By.ID, "_desktop_logo")
    SEARCH_WIDGET = (By.ID, "search_widget")
    FIELD_EMAIL = (By.ID, "field-email")
    FIELD_PASSWORD = (By.ID, "field-password")
    FOOTER = (By.ID, "footer")

    def is_opened(self):
        assert self.find_element(self.FIELD_EMAIL)
        assert self.find_element(self.FIELD_PASSWORD)
