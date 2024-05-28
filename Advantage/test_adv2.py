from playwright.sync_api import Playwright, sync_playwright, expect
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.advantageonlineshopping.com/")
    page.goto("https://www.advantageonlineshopping.com/#/")
    page.get_by_role("link", name="CONTACT US").click()
    time.sleep(4)
    page.get_by_role("link", name="OUR PRODUCTS").click()
    time.sleep(4)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
