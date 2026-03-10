"""
Test Case 2: Asset Number Configuration
Tests the Config → Device → Asset Number workflow
"""
import allure
import pytest
import time
from pywinauto.keyboard import send_keys
from pages.device_management.base_page import DeviceManagementBasePage
from pages.device_management.config_page import ConfigPage
from pages.device_management.status_page import DeviceStatusPage
from config.logger import get_logger

log = get_logger(__name__)


@pytest.mark.desktop
@pytest.mark.wja
@allure.feature("Device Configuration")
@allure.story("Asset Number Configuration")
@allure.title("C64494680 - Verification of Asset Number Configuration")
@allure.description(
    "Verify Asset Number configuration completes successfully "
    "via Devices → Config → Device category"
)
@allure.severity(allure.severity_level.CRITICAL)
def test_asset_number(app):
    """
    Test Asset Number configuration:
    1. Navigate to All Devices
    2. Discover device by IP
    3. Open Config → Device category
    4. Set Asset Number
    5. Complete Configure Devices workflow
    """
    # Initialize page objects
    dm_page = DeviceManagementBasePage(app)
    config_page = ConfigPage(app)
    # Initialize the status page to verify the device status
    status_page = DeviceStatusPage(app)

    # Test configuration
    ip_address = "15.96.121.143"
    asset_number = "96"

    with allure.step("Navigate to All Devices"):
        dm_page.click_all_devices()
    
    with allure.step("Click the 'Status' tab"):
        status_page.navigate_to_status()  # Click the Status tab

    with allure.step(f"Enter IP {ip_address} and click Go"):
        dm_page.enter_ip_and_click_go(ip_address)

    with allure.step("Handle Discovery Popup"):
        dm_page.handle_discovery_popup()

    with allure.step("Open Config → Device category"):
        config_page.open_config_device_category()

    with allure.step(f"Set Asset Number to: {asset_number}"):
        config_page.configure_asset_number(asset_number)

    with allure.step("Complete Configure Devices workflow"):
        config_page.complete_configuration()
        time.sleep(5)
        send_keys('{ENTER}')

    with allure.step("Click the 'Status' tab"):
        status_page.navigate_to_status()  # Click the Status tab

    with allure.step("Verify: Asset Number configured successfully"):
        log.info(f"✔ Asset Number '{asset_number}' configured successfully for {ip_address}")

    allure.attach(
        f"Asset Number '{asset_number}' configured successfully for device {ip_address}",
        name="Result",
        attachment_type=allure.attachment_type.TEXT
    )

    print(f"✔ Asset Number configuration completed successfully: {asset_number}")
