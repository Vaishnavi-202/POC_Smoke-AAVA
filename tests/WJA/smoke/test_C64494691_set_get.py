import pytest
import allure
import time
from pages.device_management.base_page import DeviceManagementBasePage
from pages.device_management.config_page import ConfigPage


@pytest.mark.wja
@allure.feature("Device Discovery")
@allure.story("SNMP Configuration")
@allure.title("Device Discovery and SNMP Configuration")
def test_discover_device_by_ip(app):
    """
    Test device discovery and SNMP configuration flow:
    1. Enter IP in Quick Device Discovery
    2. Navigate to Config → Security
    3. Configure SNMP Read/Write access
    4. Set SNMP community names
    5. Apply device credentials
    """
    # Initialize page objects
    dm_page = DeviceManagementBasePage(app)
    config_page = ConfigPage(app)

    # Test configuration
    ip_address = "15.96.121.39"
    community_name = "Admin123"
    username = "Administrator"
    password = "07179672"

    with allure.step(f"Enter IP {ip_address} and click Go"):
        dm_page.enter_ip_and_click_go(ip_address)

    with allure.step("Handle Discovery Popup"):
        dm_page.handle_discovery_popup()

    with allure.step("Navigate to Config Tab"):
        config_page.click_config_tab()

    with allure.step("Click Security Tree Item"):
        config_page.click_security_tree_item()

    with allure.step("Handle initial Skip and Finish prompts"):
        config_page.click_skip()
        config_page.click_finish()

    with allure.step("Navigate to Config Tab again"):
        config_page.click_config_tab()

    with allure.step("Expand Security Tree"):
        config_page.expand_security_tree()

    with allure.step("Select Access Option: Read/Write"):
        config_page.select_access_option_read_write()

    with allure.step(f"Set and Get SNMP Community: {community_name}"):
        config_page.set_and_get_snmp_community_and_apply(community_name)

    with allure.step("Initiate Configure Devices"):
        config_page.click_configure_devices()

    with allure.step(f"Configure Device Credentials (Username: {username})"):
        config_page.configure_device_credentials(username, password)

    with allure.step("Wait for Configuration to Complete"):
        config_page.wait_and_click_done()
        time.sleep(10)

    allure.attach(
        f"SNMP configuration completed for {ip_address} with community: {community_name}",
        name="Result",
        attachment_type=allure.attachment_type.TEXT
    )

    print(f"✔ Device discovery and SNMP configuration completed successfully for {ip_address}")
