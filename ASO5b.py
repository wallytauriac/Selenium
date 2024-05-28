from selenium import webdriver
from selenium.webdriver.common.by import By

class GoogleSearchPage:
    def __init__(self, driver):
        self.driver = driver

    def search(self, query):
        search_bar = self.driver.find_elements(By.NAME, "q")
        search_bar.send_keys(query)
        search_bar.submit()

    def get_results(self):
        results = self.driver.find_elements(By.CLASS_NAME, "result")
        return results