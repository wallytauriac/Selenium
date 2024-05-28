import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

import logging

class CustomLogger:
    def __init__(self, log_file):
        # Initialize logging
        logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger()

    def log_message(self, level, message):
        # Log a message with the specified level
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'critical':
            self.logger.critical(message)
        else:
            raise ValueError(f"Invalid log level: {level}")

    def write_message_to_file(self, message):
        # Write a message to the log file
        with open(self.logger.handlers[0].baseFilename, 'a') as file:
            file.write(message + '\n')


class SDAUTIL:
    def __init__(self, driver, log):
        self.driver = driver
        self.lg = log
        self.driver.set_page_load_timeout(30)

    # Define utility methods
    # Example: execute_test_cases(test_cases, pom)
    def handle_alert(self):
        """
            This code is intended to handle javascript alerts
            Wait for the alert to appear
        """
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        # Switch to the alert
        alert = self.driver.switch_to.alert
        # Close the alert
        alert.dismiss()

    def handle_window(self):
        cls = ".btn - close"
        pop_win = WebDriverWait(self.driver, 20).until(EC.number_of_windows_to_be(2))
        popup_window_handle = self.driver.window_handles[1]
        self.driver.switch_to.window(popup_window_handle)
        self.driver.find_element(By.CSS_SELECTOR, cls).click()

    def retry_find_element(self, by, value, max_retries=5):
        retries = 0
        while retries < max_retries:
            try:
                elem = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((by, value)))
                elem = self.driver.find_element(by, value)
                return elem.text
            except ElementClickInterceptedException as e:
                continue
            except TimeoutException:
                retries += 1
                time.sleep(1)  # Wait before retrying
        self.lg.log_message("error", "No Such Element exception for " + value)
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

class Timecheck:
    def __init__(self):
        self.start = time.time()

    def get_duration(self):
        end = time.time()
        elapsed = end - self.start
        elapsed = f"{elapsed:.1f} seconds"
        return elapsed

    def set_start_time(self):
        return time.time()

    def get_elapsed_time(self, start):
        end = time.time()
        elapsed = end - start
        elapsed = f"{elapsed:.1f} seconds"
        return elapsed


class SDAUTILTC:
    def __init__(self, file_path):
        # Load test case data from JSON file
        with open(file_path, 'r') as file:
            self.tc_data = json.load(file)

    def get_test_cases(self):
        # Retrieve test case data from test case file by tcname into dictionary
        # Log error if no data
        test_case_data = []
        test_case_data = self.tc_data.keys()
        return test_case_data

    def get_tc_steps(self, tcname):
        # Retrieve test case step data in dictionary
        test_case = self.tc_data[tcname]
        test_desc = test_case["description"]
        test_steps = test_case.get("test_steps", [])
        return test_steps, test_desc
