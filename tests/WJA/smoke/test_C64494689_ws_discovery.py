"""
Test Case: Device Discovery using WS-Discovery
Tests complete discovery workflow with WS-Discovery only enabled
"""
import pytest
import allure

from pages.device_management.base_page import DeviceManagementBasePage
from config.logger import get_logger

log = get_logger(__name__)


@pytest.mark.desktop
@pytest.mark.wja
@allure.feature("Device Discovery")
@allure.story("Discovery Devices")
@allure.title("C64494689 - Verification of Discovery Devices using WS-Discovery")
@allure.description(
    "Verify that only WS-Discovery is enabled for Network Connected and "
    "PC Connected devices, and all other discovery options are disabled."
)
@allure.severity(allure.severity_level.CRITICAL)
def test_open_discovery_devices(app):
    """
    Test Steps:
    1. Open Device Management
    2. Open Discovery Devices from All Devices
    3. Select 'Specify settings'
    4. Validate discovery options:
       - Network Connected → ONLY WS-Discovery (IPv4 / IPv6)
       - PC Connected → ONLY WS-Discovery
    5. Navigate through wizard
    6. Start discovery
    7. Complete discovery successfully
    """

    # Initialize page object (uses merged DeviceManagementBasePage)
    discovery_page = DeviceManagementBasePage(app)

    with allure.step("Open Device Management"):
        discovery_page.open_device_management()

    with allure.step("Open Discovery Devices dialog"):
        discovery_page.open_discovery_devices()

    with allure.step("Select 'Specify settings'"):
        discovery_page.select_specify_settings()

    with allure.step("Validate Specify Discovery Options (WS-Discovery only)"):
        discovery_page.validate_specify_discovery_options()

    with allure.step("Navigate through Discovery wizard"):
        discovery_page.click_next()
        discovery_page.click_next()
        discovery_page.click_next()

    with allure.step("Start device discovery"):
        discovery_page.click_start()

    with allure.step("Verify discovery completes successfully"):
        discovery_page.click_done()

    allure.attach(
        "Discovery completed successfully using WS-Discovery only",
        name="Result",
        attachment_type=allure.attachment_type.TEXT
    )

    log.info("✔ Discovery Devices flow completed successfully using WS-Discovery only")
    print("✔ Discovery workflow completed successfully")
