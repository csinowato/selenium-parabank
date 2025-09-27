from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class TransferFundsPage(BasePage):
    AMOUNT_INPUT = (By.ID, "amount")
    FROM_ACCOUNT = (By.ID, "fromAccountId")
    TO_ACCOUNT = (By.ID, "toAccountId")
    TRANSFER_BUTTON = (By.CSS_SELECTOR, "input[value='Transfer']")
    CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, "#showResult p")
    ERROR_MESSAGE = (By.CLASS_NAME, "error")

    def transfer_funds(self, amount, from_account_index=0, to_account_index=1):
        self.send_keys(self.AMOUNT_INPUT, (str(amount)))

        # from account
        from_dropdown = Select(self.find_element(self.FROM_ACCOUNT))
        from_dropdown.select_by_index(from_account_index)

        # to account
        to_dropdown = Select(self.find_element(self.TO_ACCOUNT))
        to_dropdown.select_by_index(to_account_index)

        self.click(self.TRANSFER_BUTTON)

    def get_confirmation_message(self):
        return self.get_text(self.CONFIRMATION_MESSAGE)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
