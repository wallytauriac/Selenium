from Selenium.ASO5a import SeleniumDriver
from Selenium.ASO5b import GoogleSearchPage

# Example usage:

driver = SeleniumDriver()
google_search_page = GoogleSearchPage(driver)

google_search_page.search("Selenium")
results = google_search_page.get_results()

for result in results:
    print(result.text)

driver.quit()