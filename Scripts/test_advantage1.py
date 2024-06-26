# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAdvantage1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
  
    def wait_for_window(self, timeout = 2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_advantage1(self):
        # Test name: Advantage1
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("https://www.advantageonlineshopping.com/")
        time.sleep(5)
        # 2 | setWindowSize | 1074x624 |
        self.driver.set_window_size(1169, 624)
        self.element_present = EC.presence_of_element_located((By.LINK_TEXT, "OUR PRODUCTS"))
        WebDriverWait(self.driver, 15).until(self.element_present)
        # self.driver.implicitly_wait(15)
        # 3 | click | linkText=OUR PRODUCTS |
        self.driver.find_element(By.LINK_TEXT, "OUR PRODUCTS").click()
        # 4 | click | linkText=SPECIAL OFFER |
        self.driver.find_element(By.LINK_TEXT, "SPECIAL OFFER").click()
        # 5 | click | linkText=POPULAR ITEMS |
        self.driver.find_element(By.LINK_TEXT, "POPULAR ITEMS").click()
        # 6 | click | linkText=CONTACT US |
        self.driver.find_element(By.LINK_TEXT, "CONTACT US").click()
        # 7 | click | id=chatLogo |
        # self.vars["window_handles"] = self.driver.window_handles
        # # 8 | storeWindowHandle | root |
        # self.driver.find_element(By.ID, "chatLogo").click()
        # # 9 | selectWindow | handle=${win1021} |
        # self.vars["win1021"] = self.wait_for_window(2000)
        # # 10 | click | css=label |
        # self.vars["root"] = self.driver.current_window_handle
        # # 11 | close |  |
        # self.driver.switch_to.window(self.vars["win1021"])
        # # 12 | selectWindow | handle=${root} |
        # self.driver.find_element(By.CSS_SELECTOR, "label").click()
        # # 13 | click | name=categoryListboxContactUs |
        # self.driver.close()
        # # 14 | select | name=categoryListboxContactUs | label=Laptops
        # self.driver.switch_to.window(self.vars["root"])
        # # 15 | click | name=productListboxContactUs |
        # self.driver.find_element(By.NAME, "categoryListboxContactUs").click()
        # # 16 | select | name=productListboxContactUs | label=HP ENVY x360 - 15t Laptop
        # dropdown = self.driver.find_element(By.NAME, "categoryListboxContactUs")
        # dropdown.find_element(By.XPATH, "//option[. = 'Laptops']").click()
        # # 17 | click | name=emailContactUs |
        # self.driver.find_element(By.NAME, "productListboxContactUs").click()
        # # 18 | type | name=emailContactUs | willyT@example.com
        # dropdown = self.driver.find_element(By.NAME, "productListboxContactUs")
        # dropdown.find_element(By.XPATH, "//option[. = 'HP ENVY x360 - 15t Laptop']").click()
        # # 19 | click | name=subjectTextareaContactUs |
        # self.driver.find_element(By.NAME, "emailContactUs").click()
        # # 20 | type | name=subjectTextareaContactUs | Test Selenium
        # self.driver.find_element(By.NAME, "emailContactUs").send_keys("willyT@example.com")
        # # 21 | click | css=.splitter:nth-child(2) |
        # self.driver.find_element(By.NAME, "subjectTextareaContactUs").click()
        # # 22 | click | linkText=OUR PRODUCTS |
        # self.driver.find_element(By.NAME, "subjectTextareaContactUs").send_keys("Test Selenium")
        # # 23 | click | id=menuUserSVGPath |
        # self.driver.find_element(By.CSS_SELECTOR, ".splitter:nth-child(2)").click()
        # # 24 | mouseDown | css=.inputContainer > .invalid:nth-child(3) |
        # self.driver.find_element(By.LINK_TEXT, "OUR PRODUCTS").click()
        # # 25 | mouseUp | css=.displayed |
        # self.driver.find_element(By.ID, "menuUserSVGPath").click()
        # # 26 | click | css=.ng-isolate-scope > .ng-isolate-scope:nth-child(1) > .inputContainer |
        # element = self.driver.find_element(By.CSS_SELECTOR, ".inputContainer > .invalid:nth-child(3)")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).click_and_hold().perform()
        # # 27 | click | css=.displayed |
        # element = self.driver.find_element(By.CSS_SELECTOR, ".displayed")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).release().perform()
        # # 28 | click | css=.displayed |
        # self.driver.find_element(By.CSS_SELECTOR, ".ng-isolate-scope > .ng-isolate-scope:nth-child(1) > .inputContainer").click()
        # # 29 | click | css=.displayed |
        # self.driver.find_element(By.CSS_SELECTOR, ".displayed").click()
        # # 30 | doubleClick | css=.displayed |
        # self.driver.find_element(By.CSS_SELECTOR, ".displayed").click()
        # # 31 | click | name=username |
        # self.driver.find_element(By.CSS_SELECTOR, ".displayed").click()
        # # 32 | type | name=username | WillyT
        # element = self.driver.find_element(By.CSS_SELECTOR, ".displayed")
        # actions = ActionChains(self.driver)
        # actions.double_click(element).perform()
        # # 33 | click | css=.ng-isolate-scope > .ng-isolate-scope:nth-child(2) label |
        # self.driver.find_element(By.NAME, "username").click()
        # # 34 | type | name=password | willyT3836
        # self.driver.find_element(By.NAME, "username").send_keys("WillyT")
        # # 35 | click | id=sign_in_btn |
        # self.driver.find_element(By.CSS_SELECTOR, ".ng-isolate-scope > .ng-isolate-scope:nth-child(2) label").click()
        # # 36 | click | css=.ng-isolate-scope > .ng-isolate-scope:nth-child(2) .animated |
        # self.driver.find_element(By.NAME, "password").send_keys("willyT3836")
        # # 37 | click | css=.PopUp > div |
        # self.driver.find_element(By.ID, "sign_in_btn").click()
        # # 38 | type | name=password | willyT123
        # self.driver.find_element(By.CSS_SELECTOR, ".ng-isolate-scope > .ng-isolate-scope:nth-child(2) .animated").click()
        # # 39 | click | id=sign_in_btn |
        # self.driver.find_element(By.CSS_SELECTOR, ".PopUp > div").click()
        # # 40 | click | id=menuUserSVGPath |
        # self.driver.find_element(By.NAME, "password").send_keys("willyT123")
        # # 41 | click | css=#loginMiniTitle > .option:nth-child(1) |
        # self.driver.find_element(By.ID, "sign_in_btn").click()
        # # 42 | click | id=menuUser |
        # self.driver.find_element(By.ID, "menuUserSVGPath").click()
        # # 43 | click | css=#loginMiniTitle > .option:nth-child(2) |
        # self.driver.find_element(By.CSS_SELECTOR, "#loginMiniTitle > .option:nth-child(1)").click()
        # # 44 | click | id=menuUser |
        # self.driver.find_element(By.ID, "menuUser").click()
        # # 45 | click | css=.roboto-medium:nth-child(3) |
        # self.driver.find_element(By.CSS_SELECTOR, "#loginMiniTitle > .option:nth-child(2)").click()
        # # 46 | close |  |
        # self.driver.find_element(By.ID, "menuUser").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".roboto-medium:nth-child(3)").click()
        # self.driver.close()


if __name__ == "__main__":
    pytest.main(["test_advantage1.py", "-s"])