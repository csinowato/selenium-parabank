from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class TransferFundsPage(BasePage):
    AMOUNT_INPUT = (By.ID, "amount")
    FROM_ACCOUNT = (By.ID, "fromAccountId")
    TO_ACCOUNT = (By.ID, "toAccountId")
    FROM_ACCOUNT_OPTIONS = (By.CSS_SELECTOR, "#fromAccountId option")
    TO_ACCOUNT_OPTIONS = (By.CSS_SELECTOR, "#toAccountId option")
    TRANSFER_BUTTON = (By.CSS_SELECTOR, "input[value='Transfer']")
    CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, "#showResult .title")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "#showError .title")

    def transfer_funds(self, amount, from_account_index=0):
        self.send_keys(self.AMOUNT_INPUT, (str(amount)))

        # wait for FROM account to load options, then select
        self.wait.until(lambda d: len(d.find_elements(*self.FROM_ACCOUNT_OPTIONS)) > 0)
        Select(self.find_element(self.FROM_ACCOUNT)).select_by_index(from_account_index)

        # wait for TO to load options, then select the last account by default
        self.wait.until(lambda d: len(d.find_elements(*self.TO_ACCOUNT_OPTIONS)) > 0)
        account_numbers = Select(self.find_element(self.TO_ACCOUNT))
        account_numbers.select_by_index(len(account_numbers.options) - 1)

        self.click(self.TRANSFER_BUTTON)

    def get_confirmation_message(self):
        return self.get_text(self.CONFIRMATION_MESSAGE)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
