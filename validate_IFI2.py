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

        # Retrieve common attributes
        for attribute_name in common_attribute_list:
            attribute_value = self.input_field.get_attribute(attribute_name)
            attributes[attribute_name] = attribute_value

        # Special handling for specific types of input fields
        if self.input_field.tag_name == "input":
            input_type = self.input_field.get_attribute("type")
            if input_type == "checkbox" or input_type == "radio":
                checked = self.input_field.get_property("checked")
                attributes["checked"] = checked
            elif input_type == "text" or input_type == "password":
                value = self.input_field.get_attribute("value")
                attributes["value"] = value
        elif self.input_field.tag_name == "select":
            select = Select(self.input_field)
            selected_option = select.first_selected_option
            attributes["selected_option"] = selected_option.text
            assert selected_option.is_selected(), f"Option '{selected_option.text}' is not selected in select input field"

        # Read expected values from JSON file
        with open(expected_values_file, 'r') as json_file:
            expected_values = json.load(json_file)

        # Find attributes for the input field
        input_field_name = self.input_field.get_attribute("name")
        input_field_data = expected_values.get(input_field_name, {})
        attributes["name"] = input_field_name
        # Iterate over attributes and perform assertions
        for attribute_name, expected_value in input_field_data.items():
            actual_value = attributes.get(attribute_name)
            # If either actual or expected value is None, replace with string 'None' for comparison
            if actual_value is None:
                actual_value = 'None'
            if expected_value is None:
                expected_value = 'None'
            if actual_value is True:
                actual_value = 'True'
            if expected_value is True:
                expected_value = 'True'

            assert actual_value == expected_value, f"Attribute '{attribute_name}' of input field '{input_field_name}' has unexpected value: expected '{expected_value}', found '{actual_value}'"

        return attributes

