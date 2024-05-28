from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def process_wtype(wtype):
    print("WAIT in use: " + wtype)
    if wtype == "S":
        time.sleep(2)
    elif wtype == "I":
        driver.implicitly_wait(10)
    else:
        explicit_wait(elem)

def navigate_homepage(wtype):
    print("Home page navigation is activated.")
    for ndx in range(1, 3):
        links[ndx].click()
        process_wtype(wtype)

    x = [0, 3]
    for y in x:
        links[y].click()
        process_wtype(wtype)


def check_element(msg, elem):
    print("Element test for wait: " + msg)
    try:
        driver.find_element(By.XPATH, elem)
    except:
        print(msg + " Locator query returned no results.")
        exit(1)

def explicit_wait(elem):
    element_present = ec.presence_of_element_located((By.XPATH, elem))
    WebDriverWait(driver, 10).until(element_present)

options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.advantageonlineshopping.com/")
driver.implicitly_wait(10)

wtype = "S"
nav_control = "ON"
# msg = "Contact Us"
# elem = '//h1[text()="CONTACT US"]'
msg = "Chat Logo"
elem = '//div/img[@id="chatLogo"]'
print(driver.title)

# /html/body/header/nav/ul/li[8]/a
# links = driver.find_elements("xpath", "/html/body/header/nav/ul/li[8]/a")  # absolute path
# links = driver.find_elements("xpath", "//nav/ul/li[@class='nav-li-Links']/a")  # relative path
#################
# links = driver.find_elements(By.CLASS_NAME, "nav-li-Links")
# links = driver.find_elements(By.CLASS_NAME, "menu navLinks roboto-regular")
# links = driver.find_elements(By.CLASS_NAME, "a.menu.navLinks.roboto-regular")
links = driver.find_elements(By.XPATH, "//li[@class='nav-li-Links']/a")

# Wait Strategy Control
if nav_control == "ON":
    check_element(msg, elem)
    explicit_wait(elem)

if len(links) == 0:
    print("Locator query returned no results.")
    print(driver.page_source)
    driver.close()
    exit(1)


for link in links:
    # print(link.get_attribute("innerHTML"))
    # print(link.get_property("innerText"))
    print(link)

# Navigation Test
# wtype = "S" - request sleep between navigations
# wtype = "I" - request implicit wait between navigations
# wtype = "E" - request explicit wait between navigations
if nav_control == "ON":
    navigate_homepage(wtype)


driver.close()

if __name__ == "__main__":
    print("Main module completed")


