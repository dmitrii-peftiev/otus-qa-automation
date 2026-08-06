import logging

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.base_url = browser.base_url
        self.logger = logging.getLogger(self.__class__.__name__)

    def _get_locator_name(self, locator):
        for cls in self.__class__.mro():
            for name, value in vars(cls).items():
                if name.startswith("_"):
                    continue
                if value == locator:
                    return name.lower().replace("_", " ")
        return str(locator)

    @allure.step("Open page: {path}")
    def open(self, path=""):
        self.logger.info(f"Opening page: {self.base_url}{path}")
        self.browser.get(f"{self.base_url}{path}")

    def find_element(self, locator, time=10):
        locator_name = self._get_locator_name(locator)
        with allure.step(f"Find element: '{locator_name}'"):
            return WebDriverWait(self.browser, time).until(
                EC.visibility_of_element_located(locator),
                message=f"Element is not visible by locator: {locator}",
            )

    def find_elements(self, locator, time=10):
        locator_name = self._get_locator_name(locator)
        with allure.step(f"Find elements: '{locator_name}'"):
            return WebDriverWait(self.browser, time).until(
                EC.visibility_of_all_elements_located(locator),
                message=f"Elements are not visible by locator: {locator}",
            )

    def click(self, locator, time=10):
        locator_name = self._get_locator_name(locator)
        self.logger.info(f"Clicking element by locator: {locator}")
        with allure.step(f"Click element: '{locator_name}'"):
            element = WebDriverWait(self.browser, time).until(
                EC.element_to_be_clickable(locator),
                message=f"Element {locator} is not clickable",
            )
            element.click()
