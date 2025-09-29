import pytest
from pages.login_page import LoginPage
from pages.account_overview_page import AccountOverviewPage
from pages.open_account_page import OpenAccountPage
from utils.test_data import TestData


@pytest.mark.regression
class TestAccountManagement:

    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url):
        # auto-login before each test
        driver.get(base_url)
        login_page = LoginPage(driver)
        login_page.login(
            TestData.VALID_USER["username"], TestData.VALID_USER["password"]
        )
        self.overview_page = AccountOverviewPage(driver)

    def test_view_account_overview(self, driver):
        # verify account numbers show
        account_numbers = self.overview_page.get_account_numbers()
        assert len(account_numbers) > 0

        # verify account balances show
        balances = self.overview_page.get_account_balances()
        assert len(balances) > 0

        # verify total balance shows
        total_balance = self.overview_page.get_total_balance()
        assert "$" in total_balance

    def test_open_checking_account(self, driver):
        self.overview_page.navigate_to_open_account()
        open_account_page = OpenAccountPage(driver)
        open_account_page.open_account("CHECKING")

        confirmation = open_account_page.get_confirmation_message()
        assert "Congratulations" in confirmation

        # verify new account number shows
        new_account_number = open_account_page.get_new_account_number()
        assert new_account_number.isdigit()

    def test_open_savings_account(self, driver):
        self.overview_page.navigate_to_open_account()
        open_account_page = OpenAccountPage(driver)
        open_account_page.open_account("SAVINGS")

        confirmation = open_account_page.get_confirmation_message()
        assert "Congratulations" in confirmation

    def test_navigation_links(self, driver):
        self.overview_page.navigate_to_transfer_funds()
        assert "Transfer Funds" in driver.title

        driver.back()
        self.overview_page.navigate_to_bill_pay()
        assert "Bill Pay" in driver.title
