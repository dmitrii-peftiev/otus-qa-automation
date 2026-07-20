import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pytestmark = pytest.mark.homework_06

TIMEOUT = 10


def test_main_page(browser):
    browser.get(browser.base_url)
    wait = WebDriverWait(browser, TIMEOUT)

    assert wait.until(EC.presence_of_element_located((By.ID, "_desktop_logo")))
    assert wait.until(EC.presence_of_element_located((By.ID, "search_widget")))
    assert wait.until(EC.presence_of_element_located((By.ID, "carousel")))
    assert wait.until(EC.presence_of_element_located((By.ID, "custom-text")))
    assert wait.until(EC.presence_of_element_located((By.ID, "footer")))


def test_catalog_page(browser):
    browser.get(browser.base_url + "/3-clothes")
    wait = WebDriverWait(browser, TIMEOUT)

    assert wait.until(EC.presence_of_element_located((By.ID, "_desktop_logo")))
    assert wait.until(EC.presence_of_element_located((By.ID, "search_widget")))
    assert wait.until(EC.presence_of_element_located((By.ID, "left-column")))
    assert wait.until(EC.presence_of_element_located((By.ID, "main")))
    assert wait.until(EC.presence_of_element_located((By.ID, "footer")))


def test_product_page(browser):
    browser.get(browser.base_url + "/men/1-2-hummingbird-printed-t-shirt.html")
    wait = WebDriverWait(browser, TIMEOUT)

    assert wait.until(EC.presence_of_element_located((By.ID, "_desktop_logo")))
    assert wait.until(EC.presence_of_element_located((By.ID, "search_widget")))
    assert wait.until(
        EC.presence_of_element_located((By.ID, "product-description-short-1"))
    )
    assert wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-or-refresh")))
    assert wait.until(EC.presence_of_element_located((By.ID, "footer")))


def test_admin_login_page(browser):
    browser.get(browser.base_url + "/administration")
    wait = WebDriverWait(browser, TIMEOUT)

    assert wait.until(EC.presence_of_element_located((By.ID, "email")))
    assert wait.until(EC.presence_of_element_located((By.ID, "passwd")))
    assert wait.until(EC.presence_of_element_located((By.ID, "submit_login")))
    assert wait.until(EC.presence_of_element_located((By.ID, "stay_logged_in")))
    assert wait.until(EC.presence_of_element_located((By.ID, "forgot-password-link")))


def test_registration_page(browser):
    browser.get(browser.base_url + "/registration")
    wait = WebDriverWait(browser, TIMEOUT)

    assert wait.until(EC.presence_of_element_located((By.ID, "_desktop_logo")))
    assert wait.until(EC.presence_of_element_located((By.ID, "search_widget")))
    assert wait.until(EC.presence_of_element_located((By.ID, "field-email")))
    assert wait.until(EC.presence_of_element_located((By.ID, "field-password")))
    assert wait.until(EC.presence_of_element_located((By.ID, "footer")))
