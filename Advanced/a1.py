from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
x = False
options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
if x:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
else:
    driver = webdriver.Chrome(options=options)

driver.get("https://www.advantageonlineshopping.com/")
time.sleep(4)
driver.implicitly_wait(15)

print(driver.title)

# /html/body/header/nav/ul/li[8]/a
# links = driver.find_elements("xpath", "/html/body/header/nav/ul/li[8]/a")  # absolute path
links = driver.find_elements("xpath", "//nav/ul/li[@class='nav-li-Links']/a")  # relative path

for link in links:
    # print(link.get_attribute("innerHTML"))
    print(link.get_property("innerText"))


driver.close()

if __name__ == "__main__":
    print("Main module completed")


