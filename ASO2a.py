import time
from selenium import webdriver
from Selenium.ASO2 import SeleniumDriver
from Selenium.ASO2 import ADVCatalogPage
# Store start time
t = time.time()
# Example usage of the two classes above:
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

sd = SeleniumDriver(driver)
adv = ADVCatalogPage(driver)
# Obtain a catalog list
logged_in = adv.login()
# time.sleep(5)
if logged_in:
    results = adv.get_catalog()
    # Output catalog list
    if len(results) > 0:
        for result in results:
            print(result.text)
    else:
        print("No catalog list available.")
else:
    print("Login failed. No catalog list available.")

# Close Browser and shutdown active driver object
sd.quit()

# Store end time
e = time.time()
print("Execution time: ", round(e-t, 2), " seconds!")


if __name__ == "__main__":
    print("Bye")