import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a ChromeOptions object

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument("start-maximized")
options.add_argument("window-size=800,500")
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()

driver.get('https://www.advantageonlineshopping.com/#/')
time.sleep(2)
assert 'Advantage Shopping' in driver.title
print("Advantage Shopping value in TAB")

elem = driver.find_element(By.CLASS_NAME, 'logo')  # Find the logo
elem.click()
print("Logo found and clicked")
driver.quit()
