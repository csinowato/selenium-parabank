from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class BillPayPage(BasePage):
    PAYEE_NAME = (By.NAME, "payee.name")
    PAYEE_ADDRESS = (By.NAME, "payee.address.street")
    PAYEE_CITY = (By.NAME, "payee.address.city")
    PAYEE_STATE = (By.NAME, "payee.address.state")
    PAYEE_ZIP = (By.NAME, "payee.address.zipCode")
    PAYEE_PHONE = (By.NAME, "payee.phoneNumber")

    ACCOUNT_NUMBER = (By.NAME, "payee.accountNumber")
    VERIFY_ACCOUNT = (By.NAME, "verifyAccount")
    AMOUNT = (By.NAME, "amount")
    FROM_ACCOUNT_SELECT = (By.NAME, "fromAccountId")
    SEND_PAYMENT_BUTTON = (By.CSS_SELECTOR, "input[value='Send Payment']")
    CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, "#billpayResult p")

    def pay_bill(self, payee_data, amount, from_account_index=0):
        self.send_keys(self.PAYEE_NAME, payee_data["name"])
        self.send_keys(self.PAYEE_ADDRESS, payee_data["address"])
        self.send_keys(self.PAYEE_CITY, payee_data["city"])
        self.send_keys(self.PAYEE_STATE, payee_data["state"])
        self.send_keys(self.PAYEE_ZIP, payee_data["zip_code"])
        self.send_keys(self.PAYEE_PHONE, payee_data["phone"])
        self.send_keys(self.ACCOUNT_NUMBER, payee_data["account_number"])
        self.send_keys(self.VERIFY_ACCOUNT, payee_data["account_number"])
        self.send_keys(self.AMOUNT, str(amount))

        from_dropdown = Select(self.find_element(self.FROM_ACCOUNT_SELECT))
        from_dropdown.select_by_index(from_account_index)

        self.click(self.SEND_PAYMENT_BUTTON)

    def get_confirmation_message(self):
        return self.get_text(self.CONFIRMATION_MESSAGE)
