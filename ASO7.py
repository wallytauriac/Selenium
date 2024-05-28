from selenium import webdriver
from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SeleniumDriver:
    def __init__(self, browser):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)

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

    def get_title(self, tag_name):
        #elem = self.driver.find_element(By.TAG_NAME, tag_name)
        title = self.driver.title
        return title

    def find_element_by_tag_name(self, tag_name):
        elem2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, tag_name)))
        if elem2:
            elem = self.driver.find_elements(By.TAG_NAME, tag_name)
        else:
            elem = []
        return elem

    def find_element_by_tag_name2(self, tag_name):
        time.sleep(2)
        elem = self.driver.find_elements(By.TAG_NAME, tag_name)
        return elem

    def find_element_by_tag_name3(self, tag_name):
        elem = []
        ignored_exceptions = (TimeoutException, StaleElementReferenceException,)
        elem.append(WebDriverWait(self.driver, 20, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located((By.TAG_NAME, tag_name))))

        # while len(elem) == 0:
        #     try:
        #         # Locate the element
        #         elem.append(WebDriverWait(self.driver, 10).until(
        #             EC.presence_of_element_located((By.TAG_NAME, tag_name))))
        #         # If the locate was successful, break out of the loop
        #         break
        #     except StaleElementReferenceException:
        #         # If StaleElementReferenceException occurs, continue the loop
        #         continue
        #     except TimeoutException:
        #         continue
        return elem

    def quit(self):
        self.driver.quit()

