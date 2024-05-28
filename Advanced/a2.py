from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.advantageonlineshopping.com/")
driver.implicitly_wait(10)

print(driver.title)

# /html/body/header/nav/ul/li[8]/a
# links = driver.find_elements("xpath", "/html/body/header/nav/ul/li[8]/a")  # absolute path
# links = driver.find_elements("xpath", "//nav/ul/li[5]/a")  # relative path

for ndx in range(1, 9, 1):
    expr = "//nav/ul/li[" + str(ndx) + "]/a"
    element = driver.find_element("xpath", expr).get_property("innerHTML")
    print(str(ndx), element)
    driver.implicitly_wait(10)
    time.sleep(3)


driver.close()

if __name__ == "__main__":
    print("Main module completed")


