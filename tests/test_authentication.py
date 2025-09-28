import pytest
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.account_overview_page import AccountOverviewPage
from utils.test_data import TestData


class TestAuthentication:
    def test_valid_login(self, driver, base_url):
        driver.get(base_url)
        login_page = LoginPage(driver)

        login_page.login(
            TestData.VALID_USER["username"], TestData.VALID_USER["password"]
        )

        # verify successful login by checking that logout button is visible
        assert login_page.is_logout_button_visible()

    def test_invalid_empty_login(self, driver, base_url):
        driver.get(base_url)
        login_page = LoginPage(driver)

        login_page.login("", "")
        error_message = login_page.get_error_message()
        assert "Please enter a username and password" in error_message

    def test_register_user(self, driver, base_url):
        driver.get(base_url)
        login_page = LoginPage(driver)
        login_page.register()

        register_page = RegisterPage(driver)
        register_page.register_user(TestData.sample_user())

        success_message = register_page.get_success_message()
        assert "Your account was created successfully" in success_message

    def test_logout(self, driver, base_url):
        driver.get(base_url)
        login_page = LoginPage(driver)
        login_page.login(
            TestData.VALID_USER["username"], TestData.VALID_USER["password"]
        )

        # navigate to accounts overview page and logout
        account_overview_page = AccountOverviewPage(driver)
        account_overview_page.logout()

        # confirm that logout redirects to login page
        assert login_page.is_login_form_visible()
