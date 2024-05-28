
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.XPATH, "//input[@id='user-name']")
        self.password_field = (By.XPATH, "//input[@id='password']")
        self.login_button = (By.XPATH, "//input[@id='login-button']")
        self.dtitle = (By.XPATH, "//div[@class='login_logo']")

    def get_title(self):
        return self.driver.find_element(*self.dtitle).text

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.welcome_message = (By.XPATH, "(//div[@class='app_logo'])[1]")
        self.burger_button = (By.XPATH, "//button[@id='react-burger-menu-btn']")
        self.logout_button = (By.XPATH, "//a[@id='logout_sidebar_link']")

    def get_welcome_message_text(self):
        return self.driver.find_element(*self.welcome_message).text

    def click_burger_button(self):
        self.driver.find_element(*self.burger_button).click()

    def click_logout_button(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.logout_button).click()

