from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Click button to display Alert
driver.find_element(By.XPATH, "(//button[normalize-space()='Click for JS Alert'])[1]").click()
time.sleep(1)
# Handle alert pop-up
try:
    driver.implicitly_wait(20)
    alert = driver.switch_to.alert
    time.sleep(1)
    alert.accept()
    time.sleep(1)
except Exception as err:
    print(err)
finally:
    print("Alert detected and removed.")

# Handle another type of Javascript POP-UP (Confirm)
try:
    driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']").click()
    time.sleep(1)
    alert = driver.switch_to.alert
    time.sleep(1)
    alert.accept()
    time.sleep(1)
except Exception as err:
    print(err)
finally:
    print("Confirm Alert detected and removed.")


# Handle another type of Javascript POP-UP (Prompt)
try:
    driver.find_element(By.XPATH, "(//button[normalize-space()='Click for JS Confirm'])[1]").click()
    time.sleep(1)
    alert = driver.switch_to.alert
    time.sleep(1)
    alert.dismiss()
    time.sleep(1)
except Exception as err:
    print(err)
finally:
    print("Prompt Alert detected and removed.")

# Continue with further automation...
driver.quit()

if __name__ == "__main__":
    print("\nMain module completed")