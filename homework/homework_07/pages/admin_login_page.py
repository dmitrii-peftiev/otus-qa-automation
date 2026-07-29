from selenium.webdriver.common.by import By
from homework.homework_07.pages.base_page import BasePage


class AdminLoginPage(BasePage):
    EMAIL = (By.ID, "email")
    PASSWD = (By.ID, "passwd")
    SUBMIT_LOGIN = (By.ID, "submit_login")
    STAY_LOGGED_IN = (By.ID, "stay_logged_in")
    FORGOT_PASSWORD_LINK = (By.ID, "forgot-password-link")

    NAV_SIDEBAR = (By.ID, "nav-sidebar")
    EMPLOYEE_INFOS = (By.ID, "employee_infos")
    HEADER_LOGOUT = (By.ID, "header_logout")

    def login(self, email, password):
        self.find_element(AdminLoginPage.EMAIL).send_keys(email)
        self.find_element(AdminLoginPage.PASSWD).send_keys(password)
        self.click(AdminLoginPage.SUBMIT_LOGIN)

    def logout(self):
        self.click(AdminLoginPage.EMPLOYEE_INFOS)
        self.click(AdminLoginPage.HEADER_LOGOUT)
