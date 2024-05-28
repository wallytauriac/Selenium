from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumDriver:
    def __init__(self, browser):
        self.driver = webdriver.Chrome()

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

    def find_element_by_tag_name(self, tag_name):
        return self.driver.find_elements(By.TAG_NAME, tag_name)

    def quit(self):
        self.driver.quit()
