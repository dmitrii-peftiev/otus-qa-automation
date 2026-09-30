import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

pytestmark = pytest.mark.homework_13


@allure.feature("Swipe Test")
@allure.story("Scroll to Calendar")
def test_swipe_to_calendar(driver):
    try:
        with allure.step("Scroll until Calendar element is visible"):
            el = driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                "new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView("
                'new UiSelector().textMatches("(?i)calendar|календарь"))',
            )
    except NoSuchElementException:
        raise NoSuchElementException(
            "Target element 'Calendar' was not found after scanning the entire list."
        )

    with allure.step("Click on Calendar element"):
        el.click()

    with allure.step("Wait for details dialog to appear"):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.Button"))
        )
