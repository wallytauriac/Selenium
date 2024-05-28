from selenium import webdriver
from Selenium.Scripts.POMClass import HomePage, LoginPage2, DashBoardPage
from selenium.webdriver.common.alert import Alert

# Create Selenium WebDriver Object
driver = webdriver.Chrome()
driver.maximize_window()
print("Text Case 1: Test Opencart Home Page")
# Create Base and Home page object for OpenCart App
home_page = HomePage(driver)
home_page.navigate_to()
# Assert Link title present on this page
try:
    title = home_page.get_link_title()
    assert "Administration" == title
    # home_page.switch_to_loginpage()
except AssertionError:
    print("Either home page link text not found or it is not equal to Administration")
    print("Title Value = ", title)
    driver.quit()
    exit(1)

print("Link title = ", title)
print("Text Case 1: Completed")
print("Text Case 2: Test Opencart Login Page Display")
login_page = LoginPage2(driver)
login_page.navigate_to()
# Assert Page title present on this page
try:
    title = login_page.get_title()
    assert "Administration" == title

except AssertionError:
    print("Either login page title not found or it is not equal to Administration")
    print("Title Value = ", title)
    driver.quit()
    exit(2)

print("Login title = ", title)
print("Text Case 2: Completed")
print("Text Case 3: Test User Login Page")
login_status = login_page.login("demo", "demo")
print("Login_status: ", login_status)
dashboard_page = DashBoardPage(driver)

try:
    title = dashboard_page.get_title()
    assert "Dashboard" == title
    dashboard_page.logout()
    print("Logout Completed successfully")
except AssertionError:
    print("Either login page title not found or it is not equal to Dashboard")
    print("Title Value = ", title)
    driver.quit()
    exit(3)

print("Dashboard title = ", title)
print("Text Case 3: Completed")

# Continue testing other pages as needed
driver.quit()

if __name__ == "__main__":
    print("Bye")