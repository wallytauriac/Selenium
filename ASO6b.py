import time

from Selenium.ASO6a import SeleniumDriver as sd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class AdvantageOnlineShoppingPage:

    @staticmethod
    def get_page_title(driver, log):
        # title = driver.find_element(By.XPATH, "//html/head/title")
        title = driver.title
        log.append("Page Title: " + title)
        return title

    @staticmethod
    def test_response(element, log):
        if element != "None":
            element.click()
            log.append("Page displayed for " + element.text)
        else:
            log.append("Link not found")

    @staticmethod
    def test_page_menu(driver, log):

        # Go to SPECIAL OFFER Page
        # element_present = EC.presence_of_element_located((By.LINK_TEXT, "OUR PRODUCTS"))
        element_present = EC.presence_of_all_elements_located((By.LINK_TEXT, "OUR PRODUCTS"))
        WebDriverWait(driver, 30).until(element_present)
        element = sd.find_element_by_link_text(driver, "SPECIAL OFFER")
        AdvantageOnlineShoppingPage.test_response(element, log)
        # Got to POPULAR ITEMS Page
        element = sd.find_element_by_link_text(driver, "POPULAR ITEMS")
        AdvantageOnlineShoppingPage.test_response(element, log)
        # Got to linkText=CONTACT US Page
        element = sd.find_element_by_link_text(driver, "CONTACT US")
        AdvantageOnlineShoppingPage.test_response(element, log)
        # Return to main page
        element = sd.find_element_by_link_text(driver, "OUR PRODUCTS")
        AdvantageOnlineShoppingPage.test_response(element, log)

    @staticmethod
    def test_contactus(driver, log):
        vars = {}
        # Got to linkText=CONTACT US Page
        element = sd.find_element_by_link_text(driver, "CONTACT US")
        AdvantageOnlineShoppingPage.test_response(element, log)
        time.sleep(2)
        # 7 | click | id=chatLogo |
        vars["window_handles"] = driver.window_handles
        # 8 | storeWindowHandle | root |
        driver.find_element(By.ID, "chatLogo").click()
        log.append("Page Navigation: Chat Box displayed for chatLogo")
        # 9 | selectWindow | handle=${win1021} |
        vars["win1021"] = sd.wait_for_window(driver, vars)
        # 10 | click | css=label |
        vars["root"] = driver.current_window_handle
        # 11 | close |  |
        driver.switch_to.window(vars["win1021"])   # This is the Chat window
        driver.close()   # Close the chat window
        log.append("Page Navigation: Chat Box closed for chatLogo")
        # 14 | select | name=categoryListboxContactUs | label=Laptops
        driver.switch_to.window(vars["root"])
        # 15 | click | name=productListboxContactUs |
        driver.find_element(By.NAME, "categoryListboxContactUs").click()
        # 16 | select | name=productListboxContactUs | label=HP ENVY x360 - 15t Laptop
        dropdown = driver.find_element(By.NAME, "categoryListboxContactUs")
        dropdown.find_element(By.XPATH, "//option[. = 'Laptops']").click()
        log.append("Selected LAPTOPS Option")
        # 17 | click | name=emailContactUs |
        driver.find_element(By.NAME, "productListboxContactUs").click()
        # 18 | type | name=emailContactUs | willyT@example.com
        log.append("Email entered: willyT@example.com")
        time.sleep(3)
        dropdown = driver.find_element(By.CSS_SELECTOR, "select[name='productListboxContactUs']")
        # (// select[@ name='productListboxContactUs'])[1]
        selection = "//option[. = 'HP ENVY x360 - 15t Laptop']"
        dropdown.find_element(By.XPATH, selection).click()
        log.append("Dropdown Selection: " + selection)
        # 19 | click | name=subjectTextareaContactUs |
        driver.find_element(By.NAME, "emailContactUs").click()
        # 20 | type | name=subjectTextareaContactUs | Test Selenium
        driver.find_element(By.NAME, "emailContactUs").send_keys("willyT@example.com")
        # 21 | click | css=.splitter:nth-child(2) |
        driver.find_element(By.NAME, "subjectTextareaContactUs").click()
        # 22 | click | linkText=OUR PRODUCTS |
        driver.find_element(By.NAME, "subjectTextareaContactUs").send_keys("Test Selenium")
        log.append("Text Area Entry: Test Selenium")
        # 23 | click | id=menuUserSVGPath |
        driver.find_element(By.CSS_SELECTOR, ".splitter:nth-child(2)").click()
        # 24 | mouseDown | css=.inputContainer > .invalid:nth-child(3) |
        element = sd.find_element_by_link_text(driver, "OUR PRODUCTS")
        AdvantageOnlineShoppingPage.test_response(element, log)