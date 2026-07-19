import pytest
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pytestmark = pytest.mark.homework_06

TIMEOUT = 10
ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "Admin123!"


def test_admin_login_logout(browser):
    browser.get(browser.base_url + "/administration")
    wait = WebDriverWait(browser, TIMEOUT)

    email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
    password_input = wait.until(EC.presence_of_element_located((By.ID, "passwd")))
    submit_button = wait.until(EC.presence_of_element_located((By.ID, "submit_login")))

    email_input.send_keys(ADMIN_EMAIL)
    password_input.send_keys(ADMIN_PASSWORD)
    submit_button.click()

    assert wait.until(EC.presence_of_element_located((By.ID, "nav-sidebar")))

    wait.until(EC.presence_of_element_located((By.ID, "employee_infos"))).click()
    wait.until(EC.presence_of_element_located((By.ID, "header_logout"))).click()

    assert wait.until(EC.presence_of_element_located((By.ID, "email")))


def test_add_random_product_to_cart(browser):
    browser.get(browser.base_url)
    wait = WebDriverWait(browser, TIMEOUT)

    products = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "thumbnail-top"))
    )
    random_product = random.choice(products)
    random_product.click()

    add_to_cart_btn = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "add-to-cart"))
    )
    add_to_cart_btn.click()

    cart_modal = wait.until(EC.presence_of_element_located((By.ID, "blockcart-modal")))
    assert cart_modal.is_displayed()


def test_currency_switch_on_main_page(browser):
    browser.get(browser.base_url)
    wait = WebDriverWait(browser, TIMEOUT)

    initial_price = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "price"))
    ).text

    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#_desktop_currency_selector button")
        )
    ).click()
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "USD $"))).click()

    new_price = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "price"))
    ).text

    assert initial_price != new_price


def test_currency_switch_in_catalog(browser):
    browser.get(browser.base_url + "/3-clothes")
    wait = WebDriverWait(browser, TIMEOUT)

    initial_price = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "price"))
    ).text

    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#_desktop_currency_selector button")
        )
    ).click()
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "USD $"))).click()

    new_price = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "price"))
    ).text

    assert initial_price != new_price
