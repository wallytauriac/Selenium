from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Don't forget about: https://selenium.dev
# Optional approach to add options to the WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
##### driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open login page in the first tab
driver.get('https://example.com/login')
time.sleep(1)

# Perform login steps...

# Open a new tab for additional tasks
driver.execute_script("window.open('https://example.com', 'newtab')")
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH, "(//a[normalize-space()='More information...'])[1]").click()
time.sleep(1)
# Check page
title = driver.find_element(By.TAG_NAME, "h1").text
print("New Window Title: ", title)
time.sleep(1)

window_handles = driver.window_handles
driver.switch_to.window(driver.window_handles[1])  # same window?

# Perform additional tasks in the new tab...

time.sleep(2)
# Closing Windows and Tabs (Because of options set, the browser remains open
# driver.quit() or driver.close()

if __name__ == "__main__":
    print("\nMain module completed")