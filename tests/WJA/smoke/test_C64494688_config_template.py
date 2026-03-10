import pytest
import allure

from pages.device_management.configuration_page import ConfigurationPage


@allure.title("Create and Apply Configuration Template Successfully")
def test_create_and_apply_configuration_template(app):

    page = ConfigurationPage(app)

    TEMPLATE_NAME = "Config Temp 1"
    MODEL_NAME = "HP DESIGNJET 10PS"

    page.focus_window()

    # Step 1–2: Navigate and create
    page.click_device_management()
    page.open_templates_tree()
    page.right_click_templates_and_create()

    # Step 3: Select model
    page.search_and_select_model(MODEL_NAME)

    # Step 4: Specify options
    page.specify_template_options(TEMPLATE_NAME)

    # Step 5: Create + apply
    page.create_template()
    page.apply_template_and_finish_creation()

    # Step 6: Apply template to device
    page.apply_template_to_devices(TEMPLATE_NAME)
    
