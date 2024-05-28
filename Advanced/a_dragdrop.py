from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# Set up the WebDriver (make sure to use the appropriate driver for your browser)
# Optional approach to add options to the WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
##### driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the demo page
driver.get("https://jqueryui.com/droppable/")

# Allow time for the page to fully load
time.sleep(2)
# Step 1: Locate the frame and switch to it
element = EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '.demo-frame'))
WebDriverWait(driver, 20).until(element)

# Step 2: Locate the draggable element (the "Draggable 1" box in this case)
draggable = driver.find_element(By.CSS_SELECTOR, ".ui-draggable")

# Step 3: Locate the droppable area (the drop area box)
droppable = driver.find_element(By.CSS_SELECTOR, ".ui-droppable")

# Step 4: Perform the drag-and-drop action using ActionChains
actions = ActionChains(driver)
actions.drag_and_drop(draggable, droppable).perform()

# Step 5: Capture the value to confirm the result
dropped_text = driver.find_element(By.CSS_SELECTOR, "#droppable>p").text
print("Dropped Value: ", dropped_text)
# Allow time to observe the result
time.sleep(1)

# Close the driver
# driver.quit()


if __name__ == "__main__":
    print("\nMain module completed")