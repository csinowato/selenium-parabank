import pytest
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.account_overview_page import AccountOverviewPage
from pages.open_account_page import OpenAccountPage
from pages.transfer_funds_page import TransferFundsPage
from pages.bill_pay_page import BillPayPage
from utils.test_data import TestData
import time


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.e2e
class TestE2EBankingWorkflow:

    # Test complete workflow: Register -> Login -> Open Account -> Transfer -> Bill Pay -> Logout
    def test_complete_new_user_journey(self, driver, base_url):
        # step 1: register new user
        driver.get(base_url)
        login_page = LoginPage(driver)
        login_page.register()

        register_page = RegisterPage(driver)
        register_page.register_user(TestData.sample_user())
        success_message = register_page.get_success_message()
        assert "Your account was created successfully" in success_message

        # step 2: login with new account (auto-login after registration)
        overview_page = AccountOverviewPage(driver)
        assert overview_page.is_logout_button_visible()

        # step 3: open a new savings account
        overview_page.navigate_to_open_account()
        open_account_page = OpenAccountPage(driver)
        open_account_page.open_account("SAVINGS")
        confirmation = open_account_page.get_confirmation_message()
        assert "Congratulations" in confirmation

        # step 4: transfer funds between accounts
        overview_page.navigate_to_transfer_funds()
        transfer_page = TransferFundsPage(driver)
        transfer_page.transfer_funds(25.00)
        transfer_confirmation = transfer_page.get_confirmation_message()
        assert "Transfer Complete" in transfer_confirmation

        # step 5: pay bill
        overview_page.navigate_to_bill_pay()
        bill_pay_page = BillPayPage(driver)
        bill_pay_page.pay_bill(TestData.SAMPLE_PAYEE, 15)
        bill_pay_confirmation = bill_pay_page.get_confirmation_message()
        assert "Bill Payment" in bill_pay_confirmation

        # step 6: logout
        overview_page.logout()
        assert login_page.is_login_form_visible()

    # Test workflow with existing user: Login -> Multiple Transactions -> Logout
    def test_existing_user_banking_session(self, driver, base_url):
        # step 1: login with existing user
        driver.get(base_url)
        login_page = LoginPage(driver)
        login_page.login(
            TestData.VALID_USER["username"], TestData.VALID_USER["password"]
        )

        # step 2: verify account balances show
        overview_page = AccountOverviewPage(driver)
        assert len(overview_page.get_account_numbers()) > 0
        assert "$" in overview_page.get_total_balance()

        # step 3: perform multiple transfers
        transfer_page = TransferFundsPage(driver)
        for amount in [10.00, 25.00, 50.00]:
            overview_page.navigate_to_transfer_funds()
            transfer_page.transfer_funds(amount)
            transfer_confirmation = transfer_page.get_confirmation_message()
            assert "Transfer Complete" in transfer_confirmation

        # step 4: pay multiple bills
        bill_pay_page = BillPayPage(driver)
        for amount in [30.00, 85.00]:
            overview_page.navigate_to_bill_pay()
            bill_pay_page.pay_bill(TestData.SAMPLE_PAYEE, amount)
            bill_pay_confirmation = bill_pay_page.get_confirmation_message()
            assert "Bill Payment" in bill_pay_confirmation

        # step 5: logout
        overview_page.logout()
        assert login_page.is_login_form_visible()
