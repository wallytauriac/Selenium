import json
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class InputFieldInspector:
    def __init__(self, input_field):
        self.input_field = input_field

    def inspect_attributes(self, expected_values_file):
        attributes = {}
        # List of common attributes to examine
        common_attribute_list = ["type", "placeholder", "maxlength", "readonly", "disabled", "required"]

        for attribute_name in common_attribute_list:
            attribute_value = self.input_field.get_attribute(attribute_name)
            attributes[attribute_name] = attribute_value

        # Additional attributes for specific types of input fields
        if self.input_field.tag_name == "input":
            input_type = self.input_field.get_attribute("type")
            if input_type == "checkbox" or input_type == "radio":
                checked = self.input_field.get_property("checked")
                attributes["checked"] = checked
            elif input_type == "text" or input_type == "password":
                value = self.input_field.get_attribute("value")
                attributes["value"] = value
        elif self.input_field.tag_name == "select":
            marital_status_select = Select(self.input_field)
            marital_status_select.select_by_value("married")
            # Special handling for select elements
            selected_option = self.input_field.find_element(By.CSS_SELECTOR, "option:checked")
            attributes["selected_option"] = selected_option.text
            if selected_option.text:
                selected_option = self.input_field.find_element(By.XPATH,
                    f".//option[text()='{selected_option.text}']")

        #return attributes

        # Perform assertions using expected values from JSON file
        # Read expected values from JSON file
        with open(expected_values_file, 'r') as json_file:
            expected_values = json.load(json_file)

        # Find attributes for the input field
        input_field_name = self.input_field.get_attribute("name")
        if input_field_name in expected_values:
            input_field_data = expected_values[input_field_name]
        else:
            input_field_data = {}

        # Iterate over attributes and perform assertions
        for attribute_name, expected_value in input_field_data.items():
            actual_value = self.input_field.get_attribute(attribute_name)
            attributes.setdefault(attribute_name, actual_value)
            if self.input_field.tag_name == "select":
                assert selected_option.is_selected(), f"Option '{selected_option.text}' is not selected in select input field '{input_field_name}'"
            else:
                assert actual_value == expected_value, f"Attribute '{attribute_name}' of input field '{input_field_name}' has unexpected value: expected '{expected_value}', found '{actual_value}'"

        return attributes

