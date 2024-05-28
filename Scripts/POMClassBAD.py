import time
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.set_page_load_timeout(30)
        self.alert = Alert(self.driver)
        self.POMUTIL = POMUTIL()

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
        POMUTIL.take_screenshot(self.driver, "datagen/ocartHome.png")
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
        POMUTIL.take_screenshot(self.driver, "datagen/ocartLogin.png")
        time.sleep(2)

    def get_title(self):
        # Get page title
        time.sleep(1)
        return self.driver.title

    def login(self, username, password):

        # element = find_by_wait(self.driver, By.ID, "input-username")
        element = self.driver.find_element(self.driver, By.ID, "input-username")

        self.driver.find_element(By.ID, "input-username").click()
        self.driver.find_element(By.ID, "input-username").send_keys(username)
        self.driver.find_element(By.ID, "input-password").click()
        self.driver.find_element(By.ID, "input-password").send_keys(password)
        POMUTIL.take_screenshot(self.driver, "datagen/ocartLogin2.png")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        time.sleep(4)
        POMUTIL.take_screenshot(self.driver, "datagen/ocartDash.png")
        return "LoggedIn"

class DashBoardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def get_title(self):
        # Get page title
        time.sleep(.5)
        return self.driver.title

    def logout(self):
        # Locate and click logout button
        time.sleep(3)
        POMUTIL.take_screenshot(self.driver, "datagen/ocartDash2.png")
        logoff = "a[class='nav-link']"
        # element = POMUTIL.find_by_wait(self.driver, By.CSS_SELECTOR, logoff, type="presence")
        element = POMUTIL.retry_find_element(self.driver, By.CSS_SELECTOR, logoff)
        try:
            element.click()
        except ElementClickInterceptedException as e:
            ha_code = "N"
            hw_code = "N"
            time.sleep(4)
            # Call Alert Handler if alert present
            if ha_code == "Y":
                POMUTIL.handle_alert(self.driver)

            # Action Chain example ued to click anywhere on the webpage to remove popup window
            body = self.driver.find_element(By.TAG_NAME, "body")
            ActionChains(self.driver).move_to_element(body).click().perform()

            # Call Window Handler if popup window present
            if hw_code == "Y":
                POMUTIL.handle_window(self.driver)

            time.sleep(1)
            element = POMUTIL.retry_find_element(self.driver, By.CSS_SELECTOR, logoff)
            element.click()
        time.sleep(2)
        POMUTIL.take_screenshot(self.driver, "datagen/ocartDash3.png")

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

class POMUTIL:
    def handle_alert(self, driver):
        """
            This code is intended to handle javascript alerts
            Wait for the alert to appear
        """
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        # Switch to the alert
        alert = driver.switch_to.alert
        # Close the alert
        alert.dismiss()

    def handle_window(self, driver):
        cls = ".btn - close"
        pop_win = WebDriverWait(driver, 20).until(EC.number_of_windows_to_be(2))
        popup_window_handle = driver.window_handles[1]
        driver.switch_to.window(popup_window_handle)
        driver.find_element(By.CSS_SELECTOR, cls).click()

    def retry_find_element(self, driver, by, value, max_retries=5):
        retries = 0
        while retries < max_retries:
            try:
                return driver.find_element(by, value)
            except ElementClickInterceptedException as e:
                continue
            except TimeoutException:
                retries += 1
                time.sleep(3)  # Wait before retrying
        raise NoSuchElementException(f"Element not found: {value}")

    def find_by_wait(self, driver, by, value, type="visible"):
        if type == "visible":
            element = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((by, value))
            )
        else:
            element = EC.presence_of_element_located((by, value))
            WebDriverWait(driver, 20).until(element)
        return element

    def take_screenshot(self, driver, name):
        os.makedirs(os.path.join("screenshot", os.path.dirname(name)), exist_ok=True)
        driver.save_screenshot(os.path.join("screenshot", name))