import time

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from Selenium.Scripts.TOMClass1 import TOMWebTests as TW
from Selenium.Scripts.POMUTIL import POM_Utility as PU


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.set_page_load_timeout(30)
        self.alert = Alert(self.driver)
        self.PU = PU()
        self.TW = TW()

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.opencart.com/index.php?route=cms/demo"
        # self.driver.implicitly_wait(20)

    def navigate_to(self):
        self.driver.get(self.url)
        # Add any additional logic needed to verify page load
        time.sleep(2)

# Add appropriate methods to manage viewing images that represent products for sale
    def get_link_title(self):
        title = self.driver.find_element(By.CSS_SELECTOR, "div[class='col-sm-6'] h2")
        self.PU.take_screenshot(self.driver, "datagen/ocartHome.png")
        return title.text

    def switch_to_loginpage(self):

        lp_button = self.driver.find_element(By.CSS_SELECTOR, "span[class='hidden-xs']")
        lp_button.click()
        time.sleep(3)

class LoginPage2(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demo.opencart.com/admin/"


    def navigate_to(self):
        self.driver.get(self.url)
        # Add any additional logic needed to verify page load
        self.PU.take_screenshot(self.driver, "datagen/ocartLogin.png")
        time.sleep(2)

    def get_title(self):
        # Get page title
        time.sleep(1)
        return self.driver.title

    def login(self, username, password):

        # element = find_by_wait(self.driver, By.ID, "input-username")
        element = self.PU.retry_find_element(self.driver, By.ID, "input-username")
        msg = self.TW.test_input_object(self.driver, By.ID, "input-username", username)
        msg = self.TW.test_input_object(self.driver, By.ID, "input-password", password)
        self.PU.take_screenshot(self.driver, "datagen/ocartLogin2.png")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        time.sleep(4)
        self.PU.take_screenshot(self.driver, "datagen/ocartDash.png")
        return "LoggedIn"

class DashBoardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def get_title(self):
        # Get page title
        time.sleep(2)
        return self.driver.title

    def logout(self):
        # Locate and click logout button
        time.sleep(3)
        self.PU.take_screenshot(self.driver, "datagen/ocartDash2.png")
        logoff = "a[class='nav-link']"
        # element = find_by_wait(self.driver, By.CSS_SELECTOR, logoff, type="presence")
        element = self.PU.retry_find_element(self.driver, By.CSS_SELECTOR, logoff)
        try:
            element.click()
        except ElementClickInterceptedException as e:
            ha_code = "N"
            hw_code = "N"
            time.sleep(4)
            # Call Alert Handler if alert present
            if ha_code == "Y":
                self.PU.handle_alert(self.driver)

            # Action Chain example ued to click anywhere on the webpage to remove popup window
            body = self.driver.find_element(By.TAG_NAME, "body")
            ActionChains(self.driver).move_to_element(body).click().perform()

            # Call Window Handler if popup window present
            if hw_code == "Y":
                self.PU.handle_window(self.driver)

            time.sleep(1)
            element = self.PU.retry_find_element(self.driver, By.CSS_SELECTOR, logoff)
            element.click()
        time.sleep(2)
        self.PU.take_screenshot(self.driver, "datagen/ocartDash3.png")

class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.opencart.com/index.php?route=account/register"

    def navigate_to(self):
        self.driver.get(self.url)
        # Add any additional logic needed to verify page load

    def register(self, username, password, email):
        pass
        # Add logic to fill in registration form and submit




