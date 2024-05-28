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



class TOMWebTests:

    def test_input_object(self, driver, by, element, value):
        try:
            driver.find_element(by, element).click()
            driver.find_element(by, element).send_keys(value)
        except TimeoutException:
            print("TOMWebTests: Timeout exception for ", element)
            exit(12)
        except NoSuchElementException:
            print("TOMWebTests: Element not found exception for ", element)
            exit(12)

        return "PASS"

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
    ## Add one or more methods to test every test needed for certain page fields to eleminate too many POM level statements



