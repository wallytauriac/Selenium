import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

class Logging:
    def __init__(self):
        # Configure logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler('test.log')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_exception(self, exception):
        self.logger.exception(exception)

    # Additional utility methods can be implemented here


class POM_Utility:

    def handle_alert(self, driver):
        """
            This code is intended to handle javascript alerts
            Wait for the alert to appear
        """
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        # Switch to the alert
        alert = driver.switch_to.alert
        # Close the alert
        alert.dismiss()

    def handle_window(self, driver):
        cls = ".btn - close"
        pop_win = WebDriverWait(driver, 20).until(EC.number_of_windows_to_be(2))
        popup_window_handle = driver.window_handles[1]
        driver.switch_to.window(popup_window_handle)
        driver.find_element(By.CSS_SELECTOR, cls).click()

    def retry_find_element(self, driver, by, value, max_retries=5):
        retries = 0
        while retries < max_retries:
            try:
                return driver.find_element(by, value)
            except ElementClickInterceptedException as e:
                continue
            except TimeoutException:
                retries += 1
                time.sleep(3)  # Wait before retrying
        raise NoSuchElementException(f"Element not found: {value}")

    def find_by_wait(self, driver, by, value, type="visible"):
        if type == "visible":
            element = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((by, value))
            )
        else:
            element = EC.presence_of_element_located((by, value))
            WebDriverWait(driver, 20).until(element)
        return element

    def take_screenshot(self, driver, name):
        os.makedirs(os.path.join("screenshot", os.path.dirname(name)), exist_ok=True)
        driver.save_screenshot(os.path.join("screenshot", name))