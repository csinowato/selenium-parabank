from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".login .button")
    REGISTER_LINK = (By.LINK_TEXT, "Register")
    ERROR_MESSAGE = (By.CLASS_NAME, "error")

    def login(self, username, password):
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def register(self):
        self.click(self.REGISTER_LINK)

    def get_error_message(self):
        self.get_text(self.ERROR_MESSAGE)
