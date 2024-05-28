import time
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from Selenium.Scripts.SDA_TOM1 import SDATOM

class BasePage:
    def __init__(self, driver, log, repo):
        self.driver = driver
        self.driver.set_page_load_timeout(30)
        self.alert = Alert(self.driver)
        self.TOM = SDATOM(self.driver, log)
        self.REPO = repo

class LoginPage(BasePage):
    def __init__(self, driver, log, repo):
        super().__init__(driver, log, repo)
        self.lg = log
        self.repo = repo
        self.url = self.REPO.get_locator('LoginPage', 'target')
        self.logo = self.REPO.get_locator('LoginPage', 'dtitle')
        self.username = self.REPO.get_locator('LoginPage', 'username')
        self.password = self.REPO.get_locator('LoginPage', 'password')
        self.button = self.REPO.get_locator('LoginPage', 'button')
        self.error_msg = self.REPO.get_locator('LoginPage', 'error')
        self.locator = {"username":self.username, "password":self.password, "button":self.button,
                        "error":self.error_msg}


    # Define methods for interacting with login page elements
    def process_page1_request(self, action):
        status = "NOK"
        steplist = action.keys()
        element = list(steplist)[4]
        if action["action"] == "navigate":
            stat = self.TOM.navigate_to(action[element])
            if stat == "OK":
                self.lg.log_message("info", "Sauce Lab Demo Site Login page accessed.")
            else:
                self.lg.log_message("error", "Sauce Lab Demo Site Login page failed access.")
                exit(1)
        elif action["action"] == "check_title":
            stat, title = self.TOM.check_title(self.logo, action[element])
            if stat == "OK":
                self.lg.log_message("info", "Page title check passed for " + title)
            else:
                self.lg.log_message("warning", "Login page title check failed. " + "Title=" + title)
        elif action["action"] == "enter_data":
            time.sleep(1)
            stat = self.TOM.enter_text(By.XPATH, self.locator[element], action[element])
            if stat == "OK":
                self.lg.log_message("info", "Data entry passed for " + element)
        # click_login_button
        elif action["action"] == "click_login_button":
            stat = self.TOM.click_element(By.XPATH, self.locator[element], action[element])
            time.sleep(1)
            if stat == "OK":
                self.lg.log_message("info", "Button click passed for " + element)
        elif action["action"] == "click_img":
            time.sleep(1)
            stat = self.TOM.click_element(By.XPATH, self.locator[element], action[element])
            if stat == "OK":
                self.lg.log_message("info", "Image click passed for " + element)
        elif action["action"] == "click_link":
            stat = self.TOM.click_element(By.XPATH, self.locator[element], action[element])
            if stat == "OK":
                time.sleep(1)
                self.lg.log_message("info", "Link click passed for " + element)
        elif action["action"] == "verify_msg":
            stat, data = self.TOM.get_text(By.CSS_SELECTOR, self.locator[element], action[element])
            if stat == "OK":
                self.lg.log_message("info", "Error message retrieved: " + data)

class CatalogPage(BasePage):
    def __init__(self, driver, log, repo):
        super().__init__(driver, log, repo)
        self.lg = log
        self.repo = repo
        self.title = self.REPO.get_locator('CatalogPage', 'dtitle')
        self.burger_menu = self.REPO.get_locator('CatalogPage', 'img')
        self.backpack = self.REPO.get_locator('CatalogPage', 'Backpack')
        self.bikelight = self.REPO.get_locator('CatalogPage', 'Bikelight')
        self.locator = {"Backlight": self.bikelight, "Backpack": self.backpack, "img":self.burger_menu}

    # Define methods for interacting with catalog page elements
    # Define methods for interacting with login page elements
    def process_page2_request(self, action):
        status = "NOK"
        steplist = action.keys()
        element = list(steplist)[4]
        if action["action"] == "navigate":
            stat = self.TOM.navigate_to(action[element])
            if stat == "OK":
                self.lg.log_message("info", "Sauce Lab Demo Site Login page accessed.")
            else:
                self.lg.log_message("error", "Sauce Lab Demo Site Login page failed access.")
                exit(1)
        elif action["action"] == "check_title":
            stat, title = self.TOM.check_title(self.title, action[element])
            if stat == "OK":
                self.lg.log_message("info", "Page title check passed for " + title)
            else:
                self.lg.log_message("warning", "Login page title check failed. " + "Title=" + title)
        elif action["action"] == "click_img":
            time.sleep(1)
            stat = self.TOM.click_element(By.XPATH, self.locator[element], action[element])
            if stat == "OK":
                self.lg.log_message("info", "Image click passed for " + element)
        elif action["action"] == "click_link":
            stat = self.TOM.click_element(By.XPATH, self.locator[element], action[element])
            if stat == "OK":
                time.sleep(1)
                self.lg.log_message("info", "Link click passed for " + element)
        elif action["action"] == "verify_msg":
            stat, data = self.TOM.get_text(By.CSS_SELECTOR, self.locator[element], action[element])
            if stat == "OK":
                self.lg.log_message("info", "Error message retrieved: " + data)

class MenuPage(BasePage):
    def __init__(self, driver, log, repo):
        super().__init__(driver, log, repo)
        self.lg = log
        self.repo = repo
        self.link = self.REPO.get_locator('MenuPage', 'link')
        self.locator = {"link": self.link}

    # Define methods for interacting with home page elements
    def process_page3_request(self, action):
        status = "NOK"
        steplist = action.keys()
        element = list(steplist)[4]
        if action["action"] == "navigate":
            time.sleep(1)
            stat = self.TOM.navigate_to(action[element])
            if stat == "OK":
                self.lg.log_message("info", "Sauce Lab Demo Site Login page accessed.")
            else:
                self.lg.log_message("error", "Sauce Lab Demo Site Login page failed access.")
                exit(1)
        elif action["action"] == "click_link":
            time.sleep(1)
            stat = self.TOM.click_element(By.XPATH, self.locator[element], action[element])
            if stat == "OK":
                self.lg.log_message("info", "Link click passed for " + element)


class ItemPage(BasePage):
    def __init__(self, driver, log, repo):
        super().__init__(driver, log, repo)
        self.lg = log
        self.repo = repo
        self.title = self.REPO.get_locator('ItemPage', 'dtitle')
        self.backpack = self.REPO.get_locator('ItemPage', 'Backpack')

    # Define methods for interacting with item page elements
