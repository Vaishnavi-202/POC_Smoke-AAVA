import pytest
import allure
from pages.device_management.base_page import DeviceManagementBasePage
from pages.device_management.alerts_page import AlertsPage
from pages.device_management.status_page import DeviceStatusPage



@pytest.mark.wja
@allure.feature("Alerts")
@allure.story("Alert Subscription")
@allure.title("C64494676 - Verification of Alert Subscription and Apply to the Devices")
def test_alert_subscription_for_device(app):
    """
    Test: Verification of Alert Subscription and Apply to the Devices
    Creates subscription with only Media Path alert enabled
    """
    # Initialize page objects
    dm_page = DeviceManagementBasePage(app)
    alerts_page = AlertsPage(app)
    
    ip_address = "15.96.121.143"
    subscription_name = "Test1"

     # Initialize the status page to verify the device status
    status_page = DeviceStatusPage(app)

    with allure.step("Select required device from All Devices"):
        dm_page.click_all_devices()

    with allure.step("Click the 'Status' tab"):
        status_page.navigate_to_status()  # Click the Status tab

    with allure.step(f"Enter IP {ip_address} and click Go"):
        dm_page.enter_ip_and_click_go(ip_address)

    with allure.step("Handle Discovery Popup"):
        dm_page.handle_discovery_popup()

    with allure.step("Navigate to Alerts tab and click 'Subscribe for Device Alerts'"):
        alerts_page.open_alerts()
        alerts_page.start_alert_subscription()

    with allure.step("Configure alert subscription (Media Path only)"):
        alerts_page.configure_alert_subscription()

    with allure.step("Enter subscription name and complete wizard"):
        alerts_page._enter_subscription_name(subscription_name)
        alerts_page._click_next_button()
        alerts_page._click_button_by_text("Subscribe")

    with allure.step("Verify alert subscription progress and completion"):
        alerts_page._wait_for_success_and_click_done()

    with allure.step("Open and verify alert history"):
        alerts_page.view_alert_history()

    allure.attach(
        f"Subscription '{subscription_name}' created with Media Path alert",
        name="Result",
        attachment_type=allure.attachment_type.TEXT
    )
    
    print(f"✔ Alert Subscription for device completed successfully with '{subscription_name}'")
