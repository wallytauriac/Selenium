import time
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumDriver:
    # Instantiate method or constructor for driver
    def __init__(self, driver):
        self.driver = driver  # Becomes an attribute

    def get(self, url):
        self.driver.get(url)

    def find_element_by_id(self, id):
        return self.driver.find_elements(By.ID, id)

    def find_element_by_name(self, name):
        return self.driver.find_elements(By.NAME, name)

    def find_element_by_class_name(self, class_name):
        return self.driver.find_elements(By.CLASS_NAME, class_name)

    def find_element_by_xpath(self, xpath):
        return self.driver.find_elements(By.XPATH, xpath)

    def quit(self):
        self.driver.quit()

class ADVCatalogPage:
    # Instantiate method or constructor for driver
    def __init__(self, driver):
        self.driver = driver  # Becomes an attribute

    def login(self):
        user = self.driver.find_element(By.ID, "user-name")
        user.send_keys("standard_user")
        psw = self.driver.find_element(By.ID, "password")
        psw.send_keys("secret_sauce")
        button = self.driver.find_element(By.ID, "login-button")
        button.submit()
        return "True"

    def get_catalog(self):
        # time.sleep(3)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))
        results = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        errors = [NoSuchElementException, ElementNotInteractableException]

        return results

