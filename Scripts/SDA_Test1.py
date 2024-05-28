from selenium import webdriver
from Selenium.Scripts.SDA_ROM1 import SDAREPO
from Selenium.Scripts.SDA_UOM1 import SDAUTILTC, CustomLogger, SDAUTIL, Timecheck
from Selenium.Scripts.SDA_POM1 import BasePage, LoginPage, CatalogPage, MenuPage
import time

def main():
    t = Timecheck()
    # Setup Test Environment
    driver = webdriver.Chrome()

    # Initialize class objects
    lvl = ["info", "debug", "error", "warning", "critical"]
    log = CustomLogger('C:/Users/wally/Documents/Python/Demo/Selenium/Templates/sdatest.log')
    repo = SDAREPO('C:/Users/wally/Documents/Python/Demo/Selenium/Templates/repo_data.json')
    tc = SDAUTILTC('C:/Users/wally/Documents/Python/Demo/Selenium/Templates/test_cases.json')
    ut = SDAUTIL(driver, log)
    bp = BasePage(driver, log, repo)
    lp = LoginPage(driver, log, repo)
    cp = CatalogPage(driver, log, repo)
    mp = MenuPage(driver, log, repo)
    # Capture the test case list
    test_cases = tc.get_test_cases()
    test_case_count = 0
    max_count = 3

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
            if page == "LoginPage":
                lp.process_page1_request(step)
            elif page == "CatalogPage":
                cp.process_page2_request(step)
            elif page == "MenuPage":
                mp.process_page3_request(step)
        test_case_duration = t.get_elapsed_time(start)
        log.log_message(lvl[0], "Test Case Duration: " + test_case_duration)

    # Quit WebDriver
    driver.quit()
    test_duration = t.get_duration()
    log.log_message(lvl[0], "Test Run Duration: " + test_duration)

if __name__ == "__main__":
    main()
