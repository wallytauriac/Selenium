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

driver.get('https://example.org')
time.sleep(2)
print(driver.title)

item = "a"
elem = driver.find_elements(By.TAG_NAME, item)  # Find the element
if len(elem) > 0:
    for item in elem:
        print(item.text)
else:
    print("No " + item + " exist")

driver.quit()