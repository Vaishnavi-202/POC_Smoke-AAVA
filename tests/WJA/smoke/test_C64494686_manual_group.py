import pytest
import allure
import time
from pages.device_management.all_devices_page import AllDevicesPage
from pages.device_management.group_page import GroupPage

@allure.title("WJA - Manual Group Creation from Device Selection")
@allure.description(
    "Selects a printer from All Devices, uses Context Menu to add to a new group, "
    "completes the wizard, and verifies the group exists."
)
@pytest.mark.desktop
@pytest.mark.wja
@pytest.mark.smoke
def test_add_printer_to_new_group(app):
    
    printer_model = "HP LaserJet MFP M633"
    new_group_name = "WJA_Manual_Test_Groupp"

    # Initialize Page Objects
    all_devices_page = AllDevicesPage(app)
    group_page = GroupPage(app)

    # 1️⃣ NAVIGATE TO ALL DEVICES
    with allure.step("Navigate to All Devices"):
        all_devices_page.click_all_devices()
        time.sleep(2) # Wait for grid to load

    # 2️⃣ SELECT DEVICE
    all_devices_page.select_device_by_model(printer_model)
    
    # Verify selection
    assert all_devices_page.verify_device_selection(), "Status tab not visible after selection"

    # 3️⃣ TRIGGER CONTEXT MENU & SELECT OPTION
    # We pass the model name so it can Right Click the specific row
    all_devices_page.context_add_to_new_group(printer_model)

    # 4️⃣ COMPLETE WIZARD
    with allure.step(f"Complete Wizard for Group: {new_group_name}"):
        group_page.finish_create_group_wizard(new_group_name)

    # 5️⃣ VERIFY GROUP CREATION
    with allure.step("Verify new group exists in tree"):
        group_page.select_group_in_tree(new_group_name)

    # 1️⃣1️⃣ DELETE CREATED GROUP
    with allure.step("Select and delete created group"):
        group_page.select_group(new_group_name)
        group_page.delete_group()
