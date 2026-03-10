import pytest
import allure

from pages.device_management.base_page import DeviceManagementBasePage
from pages.device_management.all_devices_page import AllDevicesPage
from pages.device_management.status_page import DeviceStatusPage


@allure.title("WJA - Quick Discovery + IP Range Device Discovery")
@allure.description(
    "Performs Quick Device Discovery first, then performs full Device Discovery "
    "using IP range from All Devices context menu."
)
@pytest.mark.desktop
@pytest.mark.wja
def test_device_discovery_full_flow(app):

    ip_quick = "172.22.1.102"
    ip_start = "12.12.121.245"
    ip_end = "12.12.121.247"

    # ---------------------------------------------------------
    # 1️⃣ QUICK DEVICE DISCOVERY (Top Panel)
    # ---------------------------------------------------------
    dm_page = DeviceManagementBasePage(app)
    status_page = DeviceStatusPage(app)

    with allure.step("Select required device from All Devices"):
        dm_page.click_all_devices()

    with allure.step("Click the 'Status' tab"):
        status_page.navigate_to_status()  # Click the Status tab

    # with allure.step(f"Quick Discovery using IP: {ip_quick}"):
    #     dm_page.enter_ip_and_click_go(ip_quick)

    # with allure.step("Handle Quick Discovery Popup"):
    #     dm_page.handle_discovery_popup()

    # ---------------------------------------------------------
    # 2️⃣ FULL DISCOVERY FROM ALL DEVICES (Context Menu)
    # ---------------------------------------------------------
    all_devices_page = AllDevicesPage(app)
    discovery_page = DeviceManagementBasePage(app)

    with allure.step("Open 'Discover devices...' from All Devices"):
        all_devices_page.open_discover_devices_dialog()

    # ---------------------------------------------------------
    # 3️⃣ CONFIGURE DISCOVERY SETTINGS
    # ---------------------------------------------------------
    with allure.step("Configure discovery: IP Range only"):
        all_devices_page.select_discovery_settings_and_ip_range()

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

    #log.info("✔ IP Range Discovery workflow completed successfully")
    print("✔ IP Range Discovery workflow completed successfully")
