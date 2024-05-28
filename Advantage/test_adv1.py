# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAdv1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
  
    def test_adv1(self):
        # Test name: Adv1
        # Step # | name | target | value | comment
        # 1 | open | / |  |
        self.driver.get("https://www.advantageonlineshopping.com/")
        # 2 | setWindowSize | 1169x624 |  |
        self.driver.implicitly_wait(10)
        self.driver.set_window_size(1169, 624)
        # 3 | click | linkText=CONTACT US |  |
        self.x = "//a[@translate='CONTACT_US']"
        self.epres = (EC.element_to_be_clickable((By.XPATH, self.x)))
        self.driver.find_element(By.LINK_TEXT, "CONTACT US").click()
        time.sleep(4)
        # 4 | click | linkText=OUR PRODUCTS |  |
        self.driver.find_element(By.LINK_TEXT, "OUR PRODUCTS").click()
        time.sleep(4)
  

if __name__ == "__main__":
    pytest.main(["test_adv1.py", "-s"])