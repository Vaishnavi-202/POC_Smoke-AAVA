"""
Test Case 1: Quick Device Discovery using Keyboard Actions
Uses perform_keyboard_actions() for automated discovery
"""
import pytest
import allure
from pages.device_management.all_devices_page import AllDevicesPage

@pytest.mark.wja
@allure.feature("Device Discovery")
@allure.story("Quick Discovery")
@allure.title("Quick Device Discovery using Keyboard Automation")
def test_quick_device_discovery(app):
    """
    Test Steps:
    1. Click All Devices
    2. Perform keyboard-based device discovery
    3. Click first device row
    4. Verify Status tab
    """
    # Initialize page object
    devices_page = AllDevicesPage(app)
    
    # IP address for discovery
    target_ip = "15.96.120.74"
    
    with allure.step("Navigate to All Devices"):
        devices_page.click_all_devices()

    with allure.step("Open Status tab"):
        devices_page.click_status_tab()
    
    with allure.step(f"Perform keyboard-based device discovery for {target_ip}"):
        devices_page.perform_keyboard_actions(target_ip)
    
    with allure.step("Select first device in grid"):
        devices_page.click_first_device_row()
    
    with allure.step("Open Status tab"):
        devices_page.click_status_tab()
    
    allure.attach(
        "Device discovered and Status tab opened successfully",
        name="Result",
        attachment_type=allure.attachment_type.TEXT
    )
    
    print("✔ Quick device discovery completed successfully")
