from contextlib import suppress

import allure
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--base-url", default="http://localhost:8081")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--base-url")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError(f"Browser {browser} is not supported")

    driver.base_url = base_url

    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    result = yield
    report = result.get_result()

    if report.when == "call" and report.failed and "browser" in item.fixturenames:
        driver = item.funcargs["browser"]
        with suppress(Exception):
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG,
            )
