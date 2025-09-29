# ParaBank Selenium Test Automation Framework

Automated testing framework for the ParaBank demo banking application, built with Selenium and pytest.

## 📋 Test Coverage

1. **Authentication Tests** ([test_authentication.py](tests/test_authentication.py))

   - Valid login with existing user
   - Invalid login with empty fields
   - User registration with valid data
   - Logout functionality
   - Access control for protected pages

2. **Account Management Tests** ([test_account_management.py](tests/test_account_management.py))

   - View account overview/dashboard
   - Account balance display
   - Open new checking account
   - Open new savings account
   - Navigate to transfer funds and bill pay pages

3. **Transaction Tests** ([test_transactions.py](tests/test_transactions.py))

   - Transfer funds between own accounts
   - Invalid transfer with non-numeric amounts
   - Successful bill payment

4. **E2E Banking Workflow Tests** ([test_e2e_banking_workflow.py](tests/test_e2e_banking_workflow.py))

   Complete user flows:

   - New user flow: Registration → Login → Open account → Transfer funds → Bill pay → Logout
   - Existing user flow: Login → Check account balances → Multiple transactions → Logout

## 🛠️ Setup & Installation

1. Set up Virtual Environment

   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate it
   source venv/bin/activate
   ```

2. Install Dependencies

   ```bash
   # Option A: Install manually
   pip install selenium pytest pytest-html webdriver-manager

   # Option B: Use requirements file
   pip install -r requirements.txt
   ```

## ⚡ Running Tests

```bash
# Run all tests
pytest -v -s

# Run tests by marker (e.g. e2e, smoke, regression)
pytest -m e2e -v

# Run specific test file
pytest tests/test_form_authentication.py -v -s

# Run specific test function
pytest tests/test_form_authentication.py::test_valid_login -v -s

# Generate HTML report
pytest --html=reports/report.html --self-contained-html
```
