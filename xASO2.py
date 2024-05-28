from http.server import BaseHTTPRequestHandler

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService # needed for Selenium 4
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.common.by import By
import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

options = webdriver.ChromeOptions()
# Next two lines needed for Selenium 3
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
#driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # Selenium 4
# http://localhost:63342/Demo/Selenium/Templates/index.html?_ijt=nk16shjh4l7vbncj6r6av984u2

driver.get('http://localhost:8000/Demo/Selenium/Templates/index.html')
driver.implicitly_wait(10)
driver.find_element(By.CLASS_NAME, "information")
driver.find_element(By.CSS_SELECTOR, "#fname")
driver.find_element(By.ID, "lname")
driver.find_element(By.NAME, "newsletter")
driver.find_element(By.LINK_TEXT, "Selenium Official Page")
driver.find_element(By.PARTIAL_LINK_TEXT, "Official Page")
driver.find_element(By.TAG_NAME, "a")
driver.find_element(By.XPATH, "//input[@value='f']")
# Relative Locators
email_locator = locate_with(By.TAG_NAME, "input").above({By.ID: "password"})
password_locator = locate_with(By.TAG_NAME, "input").below({By.ID: "email"})
cancel_locator = locate_with(By.TAG_NAME, "button").to_left_of({By.ID: "submit"})
submit_locator = locate_with(By.TAG_NAME, "button").to_right_of({By.ID: "cancel"})
email2_locator = locate_with(By.TAG_NAME, "input").near({By.ID: "lbl-email"})
submit2_locator = locate_with(By.TAG_NAME, "button").below({By.ID: "email"}).to_right_of({By.ID: "cancel"})
