from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):
    FIRST_NAME_INPUT = (By.NAME, "customer.firstName")
    LAST_NAME_INPUT = (By.NAME, "customer.lastName")
    ADDRESS_INPUT = (By.NAME, "customer.address.street")
    CITY_INPUT = (By.NAME, "customer.address.city")
    STATE_INPUT = (By.NAME, "customer.address.state")
    ZIP_CODE_INPUT = (By.NAME, "customer.address.zipCode")
    PHONE_INPUT = (By.NAME, "customer.phoneNumber")
    SSN_INPUT = (By.NAME, "customer.ssn")
    USERNAME_INPUT = (By.NAME, "customer.username")
    PASSWORD_INPUT = (By.NAME, "customer.password")
    CONFIRM_PASSWORD_INPUT = (By.NAME, "repeatedPassword")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "input[value='Register']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#rightPanel p")

    def register_user(self, user_data):
        self.send_keys(self.FIRST_NAME_INPUT, user_data["first_name"])
        self.send_keys(self.LAST_NAME_INPUT, user_data["last_name"])
        self.send_keys(self.ADDRESS_INPUT, user_data["address"])
        self.send_keys(self.CITY_INPUT, user_data["city"])
        self.send_keys(self.STATE_INPUT, user_data["state"])
        self.send_keys(self.ZIP_CODE_INPUT, user_data["zip_code"])
        self.send_keys(self.PHONE_INPUT, user_data["phone"])
        self.send_keys(self.SSN_INPUT, user_data["ssn"])
        self.send_keys(self.USERNAME_INPUT, user_data["username"])
        self.send_keys(self.PASSWORD_INPUT, user_data["password"])
        self.send_keys(self.CONFIRM_PASSWORD_INPUT, user_data["confirm_password"])
        self.click(self.REGISTER_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
