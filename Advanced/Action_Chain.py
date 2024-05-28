from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# Optional approach to add options to the WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
##### driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to website
driver.get("https://example.com")

# Locate element to hover over
element = driver.find_element(By.XPATH, "//a[normalize-space()='More information...']")

# Perform hover action and click link
action = ActionChains(driver)
action.move_to_element(element).click().perform()
time.sleep(1)
# Capture and confirm title text for new page
element2 = driver.find_element(By.XPATH, "//h1[normalize-space()='Example Domains']")
assert element2.text == "Example Domains"
print(element2.text)

# Close driver and browser
driver.quit()

if __name__ == "__main__":
    print("\nMain module completed")