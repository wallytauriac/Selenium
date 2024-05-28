from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.advantageonlineshopping.com/")
# driver.implicitly_wait(10)
element_present = ec.presence_of_element_located((By.XPATH, '//h1[text()="CONTACT US"]'))
WebDriverWait(driver, 20).until(element_present)

time.sleep(4)
print(driver.title)

# /html/body/header/nav/ul/li[8]/a
# links = driver.find_elements("xpath", "/html/body/header/nav/ul/li[8]/a")  # absolute path
# links = driver.find_elements("xpath", "//nav/ul/li[5]/a")  # relative path

for ndx in range(5, 9, 1):
    expr = "//nav/ul/li[" + str(ndx) + "]/a"
    driver.find_element("xpath", expr).click()

    element = driver.find_element("xpath", expr).get_property("innerText")
    print(element)
    # driver.implicitly_wait(20)
    time.sleep(3)
    element_present = ec.presence_of_element_located((By.XPATH, '//h1[text()="CONTACT US"]'))
    WebDriverWait(driver, 15).until(element_present)


driver.close()

if __name__ == "__main__":
    print("Main module completed")


