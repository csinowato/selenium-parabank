import pytest
from pages.login_page import LoginPage
from pages.account_overview_page import AccountOverviewPage
from pages.transfer_funds_page import TransferFundsPage
from pages.bill_pay_page import BillPayPage
from utils.test_data import TestData
import time


@pytest.mark.regression
@pytest.mark.transactions
class TestTransactions:

    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url):
        # auto-login before each test
        driver.get(base_url)
        login_page = LoginPage(driver)
        login_page.login(
            TestData.VALID_USER["username"], TestData.VALID_USER["password"]
        )
        self.overview_page = AccountOverviewPage(driver)

    def test_successful_transfer(self, driver):
        self.overview_page.navigate_to_transfer_funds()
        transfer_page = TransferFundsPage(driver)
        transfer_page.transfer_funds(10.00)

        confirmation = transfer_page.get_confirmation_message()
        assert "Transfer Complete" in confirmation

    def test_invalid_transfer(self, driver):
        self.overview_page.navigate_to_transfer_funds()
        transfer_page = TransferFundsPage(driver)
        transfer_page.transfer_funds("abcd")

        error = transfer_page.get_error_message()
        assert "Error" in error

    def test_bill_payment(self, driver):
        self.overview_page.navigate_to_bill_pay()
        bill_pay_page = BillPayPage(driver)
        bill_pay_page.pay_bill(TestData.SAMPLE_PAYEE, 75.00)

        confirmation = bill_pay_page.get_confirmation_message()
        assert "Bill Payment" in confirmation
