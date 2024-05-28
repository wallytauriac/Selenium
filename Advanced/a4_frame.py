from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")

# Switch to a frame by index
driver.switch_to.frame(0)

# Perform actions within the frame
try:
    driver.find_element(By.XPATH, "//iframe[@id='mce_0_ifr']").click()
    print("iFrame element found.\n")
except:
    print("iFrame Selenium test failed.")

try:
    element_data = driver.find_element(By.CSS_SELECTOR, "body p").text
    print("\n",element_data)

except:
    print("\nSelenium P-tag test failed. Frame switch did not process.")


# Switch back to default content
try:
    driver.switch_to.default_content()
except Exception as err:
    print(err)

# Continue with further automation...
driver.quit()

if __name__ == "__main__":
    print("\nMain module completed")