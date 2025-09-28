from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class OpenAccountPage(BasePage):
    ACCOUNT_TYPE = (By.ID, "type")
    FROM_ACCOUNT = (By.ID, "fromAccountId")
    OPEN_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "input[value='Open New Account']")
    CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, "#openAccountResult p")
    NEW_ACCOUNT_NUMBER = (By.ID, "newAccountId")

    def open_account(self, account_type="CHECKING", from_account_index=0):
        type_dropdown = Select(self.find_element(self.ACCOUNT_TYPE))
        type_dropdown.select_by_visible_text(account_type)

        # wait until the 'From Account' dropdown populates with account options
        self.wait.until(
            lambda d: len(Select(self.find_element(self.FROM_ACCOUNT)).options) > 0
        )

        # deposit account
        from_dropdown = Select(self.find_element(self.FROM_ACCOUNT))
        from_dropdown.select_by_index(from_account_index)

        self.click(self.OPEN_ACCOUNT_BUTTON)

    def get_confirmation_message(self):
        return self.get_text(self.CONFIRMATION_MESSAGE)

    def get_new_account_number(self):
        return self.get_text(self.NEW_ACCOUNT_NUMBER)
