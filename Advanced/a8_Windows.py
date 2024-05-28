from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Don't forget about: https://selenium.dev


# Initialize WebDriver for the browser you want to access and use:
# driver = webdriver.Chrome()  # Example for Chrome, choose as per your preference
# Optional approach to add options to the WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://example.com")
time.sleep(2)
print("Browser opened and URL set to Example.com")

# Opening New Windows and Tabs:
# If you want to open a new tab:
driver.switch_to.new_window('tab')
driver.get('about:blank')
print("New tab and URL set to about:blank")
driver.execute_script("window.open('about:blank', 'newtab')")
print("Another tab opened and URL set to about:blank")
time.sleep(2)

# If you want to Open a new window:
driver.switch_to.new_window('window')
driver.get("https://example.org")
print("New browser window opened and URL set to Example.org")
driver.execute_script("window.open('https://example.net', 'newwindow')")
print("New window tab opened and URL set to Example.net")

index = 0
time.sleep(2)

# Switching Between Windows and Tabs:
window_handles = driver.window_handles
# If you want to switch to a specific window/tab by window handle:
driver.switch_to.window(driver.window_handles[index])
print("Switched to first window/tab open")
time.sleep(2)
# Or Switching to the second tab:
driver.switch_to.window(driver.window_handles[1])
print("Switched to second window/tab open")
time.sleep(2)
# Closing Windows and Tabs (Because of options set, the browser remains open
# driver.quit() or driver.close()

if __name__ == "__main__":
    print("\nMain module completed")
