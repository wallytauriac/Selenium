from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import time
import os
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from Selenium.Scripts.SDA_UOM1 import CustomLogger, SDAUTIL


class SDATOM:
    def __init__(self, driver, log):
        self.driver = driver
        self.UTIL = SDAUTIL(self.driver, log)
        self.lg = log

    # Define methods for interacting with web elements
    def navigate_to(self, url):
        status = "NOK"
        try:
            self.driver.get(url)
        except Exception as err:
            log = (f"Unexpected {err=}, {type(err)=}")
            self.lg.log_message("error", log)
            raise
        status = "OK"
        time.sleep(2)
        return status

        # Add any additional logic needed to verify page load

    def check_title(self, locator, dtitle):
        title = self.UTIL.retry_find_element(By.XPATH, locator)
        if title == dtitle:
            return "OK", title
        else:
            return "NOK", title



    def enter_text(self, by, element, value):
        try:
            timeout = 20
            elem = EC.presence_of_element_located((by, element))
            WebDriverWait(self.driver, timeout).until(elem)
            self.driver.find_element(by, element).click()
            self.driver.find_element(by, element).send_keys(value)
        except TimeoutException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            self.lg.log_message("error", "Timeout exception for " + element)
            exit(12)
        except NoSuchElementException:
            self.lg.log_message("error", "Element not found exception for " + element)
            exit(12)

        return "OK"

    # Example: click_element(self, element_name)
    def click_element(self, by, element, value):
        try:
            timeout = 20
            elem = EC.presence_of_element_located((by, element))
            WebDriverWait(self.driver, timeout).until(elem)
            self.driver.find_element(by, element).click()
        except TimeoutException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            self.lg.log_message("error", "Timeout exception for " + element)
            exit(13)
        except NoSuchElementException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            self.lg.log_message("error", "Element not found exception for " + element)
            exit(13)

        return "OK"

    # Example: get_text(self, element_name)
    def get_text(self, by, element, value):
        try:
            timeout = 20
            elem = EC.presence_of_element_located((by, element))
            WebDriverWait(self.driver, timeout).until(elem)
            self.driver.find_element(by, element).click()
            data = self.driver.find_element(by, element).text
        except TimeoutException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            self.lg.log_message("error", "Timeout exception for " + element)
            exit(14)
        except NoSuchElementException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            self.lg.log_message("error", "Element not found exception for " + element)
            exit(14)

        return "OK", data


    def test_existence(self):
        pass
    ## Add logic to test the existence of test objects (find_element, find_elements

    def test_boundary(self):
        pass
    ## Add logic to test the boundaries of an object

    def test_equivalence_partitioning(self):
        pass
    ## Add logic to test objects with equivalence partitioning objectives

    def test_field_1(self):
        pass