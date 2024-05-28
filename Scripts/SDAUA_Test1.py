from selenium import webdriver
from Selenium.Scripts.SDAUA_ROM1 import SDAREPO
from Selenium.Scripts.SDAUA_UOM1 import *
from Selenium.Scripts.SDAUA_POM1 import *
import time

def select_browser():
    # Create a list of options
    options = ["Chrome", "Firefox", "Edge"]

    # Get the user's input
    choice = input("Choose Browser: Chrome, Firefox, or Edge: ")

    # Check if the user's input is valid
    if choice not in options:
        print("Invalid choice. Please choose one of the following options: Chrome, Firefox, or Edge.")
        exit(1)
    return choice

def configuration_management():
    path = 'C:/Users/wally/Documents/Python/Demo/Selenium/Templates/'
    log = path + 'sdaua_test.log'
    repo = path + 'sdaua_repodata.json'
    tc = path + 'sdaua_testcases.json'
    return log, repo, tc, path




# Setup Test Environment
browser = select_browser()
if browser == "Chrome":
    driver = webdriver.Chrome()
elif browser == "Firefox":
    driver = webdriver.Firefox()
else:
    driver = webdriver.Edge()
t = Timecheck()

# Initialize class objects
lvl = ["info", "debug", "error", "warning", "critical"]
logfile, repofile, tcfile, filepath = configuration_management()
log = CustomLogger(logfile)
repo = SDAREPO(repofile)
tc = SDAUTILTC(tcfile)
log.log_message(lvl[0], "Selected Browser for this run: " + browser)
log.log_message(lvl[0], "Selected Filepath for this run: " + filepath)
log.log_message(lvl[0], "Selected Logfile for this run: " + logfile)
log.log_message(lvl[0], "Selected REPOfile for this run: " + repofile)
log.log_message(lvl[0], "Selected TCfile for this run: " + tcfile)
ut = SDAUTIL(driver, log)
bp = BasePage(driver, log, repo)
lp = LoginPage(driver, log, repo)
cp = CatalogPage(driver, log, repo)
mp = MenuPage(driver, log, repo)
ip = ItemPage(driver, log, repo)
sp = CartPage(driver, log, repo)
kp = CheckoutPage(driver, log, repo)
op = OrderPage(driver, log, repo)


def main():

    # Capture the test case list
    test_cases = tc.get_test_cases()
    test_case_count = 0
    max_count = 3
    save_page = "None"
    # Iterate through all test cases
    for tcname in test_cases:
        test_case_count += 1
        start = t.set_start_time()
        if test_case_count > max_count:
            break
        # Get test step list and log this event
        test_steps, test_desc = tc.get_tc_steps(tcname)
        log.log_message(lvl[0], "Test Case ID: " + tcname)
        log.log_message(lvl[0], "Test Case Description: " + test_desc)
        # Execute test case steps
        for step in test_steps:
            # Get step ID and description
            step_id = step.get("step_id")
            log.log_message(lvl[0], "Test Step ID: " + step_id)
            log.log_message(lvl[0], "Test Step Description: " + step.get("description"))
            page = step["pagename"]
            process_page_request(page, save_page, step)
            save_page = page
        test_case_duration = t.get_elapsed_time(start)
        log.log_message(lvl[0], "Test Case Duration: " + test_case_duration)

    # Quit WebDriver
    driver.quit()
    test_duration = t.get_duration()
    log.log_message(lvl[0], "Test Run Duration: " + test_duration)

def process_page_request(page, save_page, step):
    if page != save_page:
        save_page = page
        new_page = 1
    else:
        new_page = 0

    if page == "LoginPage":
        lp.process_page1_request(step)
    elif page == "CatalogPage":
        cp.process_page2_request(step)
    elif page == "MenuPage":
        mp.process_page3_request(step)
    elif page == "ItemPage":
        ip.process_page4_request(step)
    elif page == "CartPage":
        sp.process_page5_request(step)
    elif page == "CheckoutPage":
        kp.process_page6_request(step)
    elif page == "OrderPage":
        op.process_page7_request(step)

    if new_page:
        ut.take_screenshot(driver, "sda/sdaua_" + page + ".png")


if __name__ == "__main__":
    main()
