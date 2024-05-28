import time
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from Selenium.Scripts.SDAUA_TOM1 import SDATOM
from Selenium.Scripts.SDAUA_UOM1 import *

class BasePage:
    def __init__(self, driver, log, repo):
        self.driver = driver
        self.driver.set_page_load_timeout(30)
        self.alert = Alert(self.driver)
        self.TOM = SDATOM(self.driver, log)
        self.REPO = repo
        self.ut = SDAUTIL(self.driver, log)

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
                self.lg.log_message("info", action["description"] + ": " + title)
            else:
                self.lg.log_message("warning", "Login page title check failed. " + "Title=" + title)
        elif action["action"] == "enter_data":
            time.sleep(1)
            stat = self.TOM.enter_text(By.XPATH, self.locator[element], action[element])
            if stat == "OK":
                self.lg.log_message("info", action["description"] + ": " + element)
                self.ut.take_screenshot(self.driver, "sda/sdaua_aft_" + "LoginPage" + ".png")
        # click_login_button
        elif action["action"] == "click_button":
            stat = self.TOM.click_element(By.XPATH, self.locator[element], action[element])
            time.sleep(1)
            if stat == "OK":
                self.lg.log_message("info", action["description"] + ": " + element)
        elif action["action"] == "click_img":
            time.sleep(1)
            stat = self.TOM.click_element(By.XPATH, self.locator[element], action[element])
            if stat == "OK":
                self.lg.log_message("info", action["description"] + ": " + element)
        elif action["action"] == "click_link":
            stat = self.TOM.click_element(By.XPATH, self.locator[element], action[element])
            if stat == "OK":
                time.sleep(1)
                self.lg.log_message("info", action["description"] + ": " + element)
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
        self.item_1 = self.REPO.get_locator('CatalogPage', 'item_1')
        self.locator = {"Backlight": self.bikelight, "Backpack": self.backpack,
                        "img":self.burger_menu, "item_1": self.item_1}

    # Define methods for interacting with catalog page elements

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
                self.lg.log_message("info", action["description"] + ": " + title)
            else:
                self.lg.log_message("warning", "Login page title check failed. " + "Title=" + title)
        elif action["action"] == "click_link":
            stat = self.TOM.click_element(By.XPATH, self.locator[element], action[element])
            if stat == "OK":
                time.sleep(1)
                self.lg.log_message("info", action["description"] + ": " + element)
        elif action["action"] == "verify_msg":
            stat, data = self.TOM.get_text(By.CSS_SELECTOR, self.locator[element], action[element])
            if stat == "OK":
                self.lg.log_message("info", "Error message retrieved: " + " - " + data)

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
            self.ut.take_screenshot(self.driver, "sda/sdaua_bfr_" + "MenuPage" + ".png")
            stat = self.TOM.click_element(By.XPATH, self.locator[element], action[element])
            if stat == "OK":
                self.lg.log_message("info", action["description"] + ": " + element)


class ItemPage(BasePage):
    def __init__(self, driver, log, repo):
        super().__init__(driver, log, repo)
        self.lg = log
        self.repo = repo
        self.title = self.REPO.get_locator('ItemPage', 'dtitle')
        self.backpack = self.REPO.get_locator('ItemPage', 'Backpack')
        self.item_1_price = self.REPO.get_locator('ItemPage', 'item_1_price')
        self.atc_button = self.REPO.get_locator('ItemPage', 'atc_button')
        self.cart_icon = self.REPO.get_locator('ItemPage', 'cart_icon')
        self.locator = {"title": self.title, "backpack": self.backpack,
                        "item_1_price": self.item_1_price, "atc_button": self.atc_button, "cart_icon": self.cart_icon}

    # Define methods for interacting with item page elements
    def process_page4_request(self, action):
        status = "NOK"
        steplist = action.keys()
        element = list(steplist)[4]
        strgy = self.REPO.get_strategy('ItemPage', element)
        by_strgy = getattr(By, strgy.upper())
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
            stat = self.TOM.click_element(by_strgy, self.locator[element], action[element])
            if stat == "OK":
                self.lg.log_message("info", action["description"] + ": " + element)
        elif action["action"] == "click_button":
            stat = self.TOM.click_element(by_strgy, self.locator[element], action[element])
            time.sleep(1)
            if stat == "OK":
                self.lg.log_message("info", action["description"] + ": " + element)
        elif action["action"] == "get_text":
            stat, data = self.TOM.get_text(by_strgy, self.locator[element], action[element])
            if stat == "OK":
                self.lg.log_message("info", action["description"]  + " - " + data)


class CartPage(BasePage):
    def __init__(self, driver, log, repo):
        super().__init__(driver, log, repo)
        self.lg = log
        self.repo = repo
        self.title = self.REPO.get_locator('CartPage', 'dtitle')
        self.item_1_price = self.REPO.get_locator('CartPage', 'item_1_price')
        self.checkout_button = self.REPO.get_locator('CartPage', 'checkout_button')
        self.locator = {"title": self.title, "item_1_price": self.item_1_price, "checkout_button": self.checkout_button}

    # Define methods for interacting with item page elements
    def process_page5_request(self, action):
        status = "NOK"
        steplist = action.keys()
        element = list(steplist)[4]
        strgy = self.REPO.get_strategy('CartPage', element)
        by_strgy = getattr(By, strgy.upper())
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
            stat = self.TOM.click_element(by_strgy, self.locator[element], action[element])
            if stat == "OK":
                self.lg.log_message("info", action["description"] + ": " + element)
        elif action["action"] == "click_button":
            stat = self.TOM.click_element(by_strgy, self.locator[element], action[element])
            time.sleep(1)
            if stat == "OK":
                self.lg.log_message("info", action["description"] + ": " + element)
        elif action["action"] == "get_text":
            stat, data = self.TOM.get_text(by_strgy, self.locator[element], action[element])
            if stat == "OK":
                self.lg.log_message("info", action["description"]  + " - " + data)


class CheckoutPage(BasePage):
    def __init__(self, driver, log, repo):
        super().__init__(driver, log, repo)
        self.lg = log
        self.repo = repo
        self.fname = self.REPO.get_locator('CheckoutPage', 'fname')
        self.lname = self.REPO.get_locator('CheckoutPage', 'lname')
        self.zip_code = self.REPO.get_locator('CheckoutPage', 'zip_code')
        self.continue_button = self.REPO.get_locator('CheckoutPage', 'continue_button')
        self.pay_info = self.REPO.get_locator('CheckoutPage', 'pay_info')
        self.total_amt = self.REPO.get_locator('CheckoutPage', 'total_amt')
        self.finish_button = self.REPO.get_locator('CheckoutPage', 'finish_button')
        self.locator = {
                        "fname": self.fname, "lname": self.lname,
                        "zip_code": self.zip_code, "continue_button": self.continue_button,
                        "pay_info": self.pay_info, "total_amt": self.total_amt, "finish_button": self.finish_button}

    # Define methods for interacting with catalog page elements

    def process_page6_request(self, action):
        status = "NOK"
        steplist = action.keys()
        element = list(steplist)[4]
        strgy = self.REPO.get_strategy('CheckoutPage', element)
        by_strgy = getattr(By, strgy.upper())
        if action["action"] == "navigate":
            stat = self.TOM.navigate_to(action[element])
            if stat == "OK":
                self.lg.log_message("info", "Sauce Lab Demo Site Login page accessed.")
            else:
                self.lg.log_message("error", "Sauce Lab Demo Site Login page failed access.")
                exit(1)
        elif action["action"] == "click_button":
            stat = self.TOM.click_element(by_strgy, self.locator[element], action[element])
            time.sleep(1)
            if stat == "OK":
                self.lg.log_message("info", action["description"] + ": " + element)
        elif action["action"] == "get_text":
            stat, data = self.TOM.get_text(by_strgy, self.locator[element], action[element])
            if stat == "OK":
                self.lg.log_message("info", action["description"] + " - " + data)
        elif action["action"] == "enter_data":
            time.sleep(1)
            stat = self.TOM.enter_text(by_strgy, self.locator[element], action[element])
            if stat == "OK":
                self.lg.log_message("info", action["description"] + ": " + action[element])
                self.ut.take_screenshot(self.driver, "sda/sdaua_aft_" + "CheckoutPage" + ".png")


class OrderPage(BasePage):
    def __init__(self, driver, log, repo):
        super().__init__(driver, log, repo)
        self.lg = log
        self.repo = repo
        self.title = self.REPO.get_locator('OrderPage', 'dtitle')
        self.img = self.REPO.get_locator('OrderPage', 'img')
        self.locator = {"title": self.title, "img": self.img}

    # Define methods for interacting with item page elements
    def process_page7_request(self, action):
        status = "NOK"
        steplist = action.keys()
        element = list(steplist)[4]
        strgy = self.REPO.get_strategy('OrderPage', element)
        by_strgy = getattr(By, strgy.upper())
        if action["action"] == "navigate":
            time.sleep(1)
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
            stat = self.TOM.click_element(by_strgy, self.locator[element], action[element])
            if stat == "OK":
                self.lg.log_message("info", action["description"] + ": " + element)
