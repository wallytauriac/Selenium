import json

class Locator:
    def __init__(self, file_path):
        # Load locator data from JSON file
        with open(file_path, 'r') as file:
            self.locator_data = json.load(file)

    def get_locator(self, page_name, element_name):
        # Retrieve locator data for specified page and element
        try:
            page_data = self.locator_data[page_name]
            element_data = page_data[element_name]
            return element_data
        except KeyError:
            raise KeyError(f"Locator not found for page '{page_name}' and element '{element_name}'")

# Usage Example:
# Instantiate Locator Class with JSON file path
locator = Locator('locators.json')

# Get locator data for login page username field
locator_data = locator.get_locator('LoginPage', 'UsernameField')
print(locator_data)
