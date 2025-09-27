from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AccountOverviewPage(BasePage):

    ACCOUNT_TABLE = (By.ID, "accountTable")
    ACCOUNT_NUMBERS = (
        By.XPATH,
        "//table[@id='accountTable']//tr[position()>1]/td[1]/a",
    )
    ACCOUNT_BALANCES = (By.XPATH, "//table[@id='accountTable']//tr[position()>1]/td[2]")
    TOTAL_BALANCES = (By.XPATH, "//table[@id='accountTable']//tr[last()]/td[2]/b")

    # Navigation Links
    OPEN_ACCOUNT_LINK = (By.LINK_TEXT, "Open New Account")
    TRANSFER_FUNDS_LINK = (By.LINK_TEXT, "Transfer Funds")
    BILL_PAY_LINK = (By.LINK_TEXT, "Bill Pay")
    LOGOUT_LINK = (By.LINK_TEXT, "Log Out")

    def get_account_numbers(self):
        account_elements = self.driver.find_elements(*self.ACCOUNT_NUMBERS)
        return [element.text for element in account_elements]

    def get_account_balances(self):
        balance_elements = self.driver.find_elements(*self.ACCOUNT_BALANCES)
        return [element.text for element in balance_elements]

    def get_total_balance(self):
        return self.get_text(self.TOTAL_BALANCE)

    def navigate_to_open_account(self):
        self.click(self.OPEN_ACCOUNT_LINK)

    def navigate_to_transfer_funds(self):
        self.click(self.TRANSFER_FUNDS_LINK)

    def navigate_to_bill_pay(self):
        self.click(self.BILL_PAY_LINK)

    def logout(self):
        self.click(self.LOGOUT_LINK)
