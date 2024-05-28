import json

class SDAREPO:
    def __init__(self, file_path):
        # Load locator data from JSON file
        with open(file_path, 'r') as file:
            self.repo_data = json.load(file)

    def get_locator(self, page_name, element_name):
        # Retrieve locator data from repository
        locator_data = self.repo_data.get(page_name, {}).get(element_name)
        if locator_data:
            return locator_data['locator']
        else:
            raise ValueError(f"Locator for element '{element_name}' on page '{page_name}' not found.")

    def get_strategy(self, page_name, element_name):
        # Retrieve locator data from repository
        locator_data = self.repo_data.get(page_name, {}).get(element_name)
        if locator_data:
            return locator_data['strategy']
        else:
            raise ValueError(f"Locator for element '{element_name}' on page '{page_name}' not found.")

# repo = SDAREPO('C:/Users/wally/Documents/Python/Demo/Selenium/Templates/repo_data.json')
# x, y = repo.get_locator('LoginPage', 'dtitle')
# print(x)
# print(y)
#
# if __name__ == "__main__":
#     print("bye")