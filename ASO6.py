import os
from selenium import webdriver
from Selenium.ASO6b import AdvantageOnlineShoppingPage as aosp

def print_log(log):
    for item in log:
        print(item)
    log.pop()

# Test Script Processor:
def main():
    log = []
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.set_window_size(1074, 624)
    # html_file_path = os.path.abspath("Selenium/Templates/Advantage.html")
    # driver.get("file://" + html_file_path)
    driver.get("https://www.advantageonlineshopping.com/#/")
    tc = 3  # Define value to control test case execution
    # Test Case 1
    if tc in (1, 12, 123):
        log.append("Test Case 1")
        aosp.get_page_title(driver, log)
        print_log(log)
    # Test Case 2
    if tc in (2, 12, 123):
        log.append("Test Case 2")
        aosp.test_page_menu(driver, log)
        print_log(log)
    # Test Case 3
    if tc in (3, 123):
        log.append("Test Case 3")
        aosp.test_contactus(driver, log)
        print_log(log)



    # Test Script Shutdown:
    driver.quit()


if __name__ == "__main__":
    main()
