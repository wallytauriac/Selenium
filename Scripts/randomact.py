from selenium import webdriver
from Selenium.ASO7 import SeleniumDriver as sd
import random
import time

# List of URLs to visit
urls = ["https://example.com", "https://example.org", "https://example.net"]

# List of elements to interact with
elements = ["link", "button", "input field", "text data"]

# List of results from interacting with elements
log = []

# Function to perform randomized actions
def randomized_actions(driver, x):
    # Visit a random URL
    random_url = random.choice(urls)
    driver.get(random_url)
    title = driver.get_title('title')

    time.sleep(4)  # Add some delay to let the page load

    x = x + 1
    log.append("Test Case #" + str(x) + "->")
    log.append("URL test for: " + random_url)
    log.append("Page processed: " + title)
    # Perform random interactions
    random_element = random.choice(elements)
    log.append("Element test for : " + random_element)
    if random_element == "link":
        # Click on a random link
        try:
            links = driver.find_element_by_tag_name('a')
        except Exception as e:
            print("Link error encountered")
            print(e.__doc__)
            print(f"Unexpected {e=}, {type(e)=}")
            exit(2)

        if len(links) > 0:
            random_link = random.choice(links)
            #random_link.click()
            log.append("Link processed: " + random_link.text)

        else:
            log.append("Element test for : " + random_element + " none found")
    elif random_element == "button":
        # Click on a random button
        try:

            buttons = driver.find_element_by_tag_name2('button')
        except Exception as e:
            print("Button error encountered")
            print(e.__doc__)
            print(f"Unexpected {e=}, {type(e)=}")
            exit(3)

        if len(buttons) > 0:
            random_button = random.choice(buttons)
            #random_button.click()
            log.append("Button processed: " + random_button.text)
        else:
            log.append("No " + random_element + " found on this page.")
    elif random_element == "input field":
        # Type in a random input field
        try:

            input_fields = driver.find_element_by_tag_name2('input')
        except Exception as e:
            print("Input error encountered")
            print(e.__doc__)
            print(f"Unexpected {e=}, {type(e)=}")
            exit(4)
        if len(input_fields) > 0:
            random_input_field = random.choice(input_fields)
            #random_input_field.send_keys("Random text")
            log.append("Field processed: " + random_input_field.text)
        else:
            log.append("Element test for : " + random_element + " not found")
    elif random_element == "text data":
        # Type in a random input field
        try:

            text_data = driver.find_element_by_tag_name('p')
        except Exception as e:
            print("Input error encountered")
            print(e.__doc__)
            print(f"Unexpected {e=}, {type(e)=}")
            exit(5)
        if len(text_data) > 0:
            random_text_data = random.choice(text_data)
            log.append("Field processed: " + random_text_data.text)
        else:
            log.append("Element test for : " + random_element + " not found")

def print_log():
    n = 0
    for line in log:
        n = n + 1
        print("Log line " + str(n) + ": " + line)

# Main function
def main():
    # Initialize Selenium WebDriver
    #driver = sd("browser")

    try:
        # Perform randomized actions
        for i in range(5):  # Repeat 5 times for demonstration
            driver = sd("browser")
            randomized_actions(driver, i)
            driver.quit()
            #time.sleep(3)  # Add some delay between actions
    except Exception as e:
        driver.quit()
        print("error encountered")
        print(e.__doc__)
        print(f"Unexpected {e=}, {type(e)=}")
        exit(1)
    finally:
        # Close the WebDriver
        #driver.quit()
        print_log()

if __name__ == "__main__":
    main()
