import pytest
import allure
from pages.device_management.base_page import DeviceManagementBasePage
from pages.device_management.status_page import DeviceStatusPage

@pytest.mark.wja
@allure.feature("Device Discovery")
def test_discover_device_by_ip(app):
    """
    Test device discovery flow:
    1. Enter IP in Quick Device Discovery (Device Management)
    2. Click Go
    3. Handle popup
    4. Verify status (click Status tab)
    """
    # Initialize the consolidated page
    dm_page = DeviceManagementBasePage(app)
    # Initialize the status page to verify the device status
    status_page = DeviceStatusPage(app)

    ip_address = "15.96.121.143"
    

    with allure.step("Select required device from All Devices"):
        dm_page.click_all_devices()

    with allure.step("Click the 'Status' tab"):
        status_page.navigate_to_status()  # Click the Status tab

    with allure.step(f"Enter IP {ip_address} and click Go"):
        dm_page.enter_ip_and_click_go(ip_address)

    with allure.step("Handle Discovery Popup"):
        dm_page.handle_discovery_popup()

    with allure.step("Click the 'Status' tab"):
        status_page.navigate_to_status()  # Click the Status tab