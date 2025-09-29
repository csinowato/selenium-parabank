from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    # # wait until element is clickable and retry on stale references
    def click(self, locator, retries=3):
        for attempt in range(retries):
            try:
                element = self.wait.until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if attempt == retries - 1:
                    raise

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
