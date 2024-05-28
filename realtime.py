from selenium import webdriver
from selenium.common import InvalidArgumentException
from selenium.webdriver.common.by import By
import time
import os

# Create a directory to store screenshots and logs
if not os.path.exists('captured_data'):
    os.makedirs('captured_data')

# Function to capture screenshot
def capture_screenshot(driver, step_number):
    screenshot_path = f"captured_data/screenshot_{step_number}.png"
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot captured: {screenshot_path}")

# Function to capture logs
def capture_logs(driver, step_number):
    try:
        logs = ["WebDriver log type = browser"]
        logs.append(driver.get_log('browser'))
        logs.append("WebDriver log type = driver")
        logs.append(driver.get_log('driver'))
        logs.append("WebDriver log type = client")
        logs.append(driver.get_log('client'))
        logs.append("WebDriver log type = server")
        logs.append(driver.get_log('server'))
    except InvalidArgumentException:
        pass

    log_path = f"captured_data/logs_{step_number}.txt"
    with open(log_path, 'w') as file:
        for log_entry in logs:
            file.write(str(log_entry) + '\n')
    print(f"Logs captured: {log_path}")

# Function to analyze captured data
def analyze_captured_data():
    screenshots = [f for f in os.listdir('captured_data') if f.startswith('screenshot')]
    logs = [f for f in os.listdir('captured_data') if f.startswith('logs')]

    print("\nCount of Captured Screenshots:", len(screenshots))
    print("Count of Captured Logs:", len(logs))

# Main function to execute tests
def main():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.example.com")
        time.sleep(4)  # Wait for page to load

        # Example test steps
        for step_number in range(1, 4):
            # Perform actions
            # For demonstration, let's click on a link
            link = driver.find_element(By.XPATH, "//a")
            link.click()

            # Capture screenshot and logs after each step
            capture_screenshot(driver, step_number)
            capture_logs(driver, step_number)

            time.sleep(2)  # Add a delay between steps

    finally:
        # Example usage
        analyze_captured_data()
        driver.quit()

if __name__ == "__main__":
    main()

