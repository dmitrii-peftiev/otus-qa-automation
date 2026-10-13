import os
from contextlib import suppress

import allure
import pytest
from appium import webdriver
from appium.options.common import AppiumOptions


@pytest.fixture(scope="function")
def driver():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    apk_path = os.path.join(current_dir, "..", "apk", "pnv.apk")
    apk_path = os.path.normpath(apk_path)

    device = os.environ.get("ANDROID_DEVICE_NAME", "")

    caps = AppiumOptions()
    caps.load_capabilities(
        {
            "platformName": "Android",
            "appium:automationName": "UiAutomator2",
            "appium:deviceName": device,
            "appium:app": apk_path,
            "appium:appPackage": "com.csdroid.pkg",
            "appium:appActivity": ".MainActivity",
            "appium:noReset": True,
            "appium:noSign": True,
        }
    )

    driver = webdriver.Remote("http://localhost:4723", options=caps)
    driver.implicitly_wait(2.0)

    yield driver

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    result = yield
    report = result.get_result()

    if report.when == "call" and report.failed and "driver" in item.fixturenames:
        driver = item.funcargs["driver"]
        with suppress(Exception), allure.step("Save screenshot on failure"):
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG,
            )
