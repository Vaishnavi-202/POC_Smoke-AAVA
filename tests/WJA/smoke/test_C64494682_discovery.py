"""
Test Case: Device Discovery using IP Range
Tests complete discovery workflow with IP range specification
"""
import pytest
import allure
from pages.device_management.base_page import DeviceManagementBasePage
from pages.device_management.status_page import DeviceStatusPage
from config.logger import get_logger

log = get_logger(__name__)


@pytest.mark.desktop
@pytest.mark.wja
@allure.feature("Device Discovery")
@allure.story("Discovery Devices")
@allure.title("C64494682 - Verification of Discovery Devices using IP Range")
@allure.description(
    "Verify that device discovery can be completed successfully using IP range "
    "specification. Test includes quick discovery followed by full IP range discovery workflow."
)
@allure.severity(allure.severity_level.CRITICAL)
def test_discover_device_by_ip_range(app):
    """
    Test Steps:
    1. Perform Quick Device Discovery for single IP
    2. Handle discovery popup
    3. Open Device Management
    4. Expand Overview section
    5. Right-click All Devices
    6. Open Discover Devices dialog
    7. Select 'Specify settings' with IP range option
    8. Configure IP range (start and end)
    9. Add IP range to discovery list
    10. Navigate through discovery wizard
    11. Start discovery process
    12. Verify discovery completes successfully
    """

    # Initialize page object
    discovery_page = DeviceManagementBasePage(app)
    status_page = DeviceStatusPage(app)

    with allure.step("Select required device from All Devices"):
        discovery_page.click_all_devices()

    with allure.step("Click the 'Status' tab"):
        status_page.navigate_to_status()  # Click the Status tab

    with allure.step("Perform Quick Device Discovery"):
        discovery_page.enter_ip_and_click_go("15.96.121.143")

    with allure.step("Handle discovery popup"):
        discovery_page.handle_discovery_popup()

    with allure.step("Click Device Management module"):
        btn = discovery_page._device_management_btn()
        btn.wait("exists enabled", timeout=10)
        btn.click_input()
        log.info("Clicked 'Device Management'")

    with allure.step("Expand Overview tree"):
        discovery_page.expand_overview()

    with allure.step("Right-click All Devices"):
        discovery_page.right_all_devices()

    with allure.step("Click Discover devices from context menu"):
        discovery_page.click_discover_devices()

    with allure.step("Select Specify settings and enable IP range"):
        discovery_page.select_discovery_settings_and_ip_range()

    with allure.step("Click Next to proceed"):
        discovery_page.click_next()

    with allure.step("Click Add button to configure IP range"):
        discovery_page.click_add_button()

    with allure.step("Enter first IP address (15.96.121.45)"):
        discovery_page.enter_first_ip_address("15.96.121.45")

    with allure.step("Enter last IP address (15.96.121.47)"):
        discovery_page.enter_last_ip_address("15.96.121.47")

    with allure.step("Click Add button in IP Range dialog"):
        discovery_page.click_add_ip_range_button()

    with allure.step("Close IP Range dialog"):
        discovery_page.click_close_ip_range_dialog()

    with allure.step("Select configured IP range row"):
        discovery_page.select_ip_range_row("15.96.121.45", "15.96.121.47")

    with allure.step("Click Next from IP range selection"):
        discovery_page.click_next_from_ip_range()

    with allure.step("Click Next to continue"):
        discovery_page.click_next()

    with allure.step("Start device discovery"):
        discovery_page.click_start()

    with allure.step("Verify discovery completes and click Done"):
        discovery_page.click_done_after_discovery()

    allure.attach(
        "Discovery completed successfully using IP range 15.96.121.45 - 15.96.121.47",
        name="Result",
        attachment_type=allure.attachment_type.TEXT
    )

    log.info("✔ IP Range Discovery workflow completed successfully")
    print("✔ IP Range Discovery workflow completed successfully")
