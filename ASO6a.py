import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class SeleniumDriver:
    @staticmethod
    def find_element_by_id(driver, id):
        return driver.find_element(By.ID, id)

    @staticmethod
    def find_element_by_name(driver, name):
        return driver.find_element(By.NAME, name)

    @staticmethod
    def find_element_by_class_name(driver, class_name):
        return driver.find_element(By.CLASS_NAME, class_name)

    @staticmethod
    def find_element_by_xpath(driver, xpath):
        return driver.find_element(By.XPATH, xpath)

    @staticmethod
    def find_element_by_tag_name(driver, tag_name):
        return driver.find_element(By.TAG_NAME, tag_name)

    @staticmethod
    def find_element_by_link_text(driver, link_text):
        time.sleep(5)
        try:
            element = driver.find_element(By.LINK_TEXT, link_text)
        except NoSuchElementException:
            return "None"
        return element

    @staticmethod
    def wait_for_window(driver, vars, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = driver.window_handles
        wh_then = vars["window_handles"]
        if len(wh_now) > len(wh_then):
          return set(wh_now).difference(set(wh_then)).pop()