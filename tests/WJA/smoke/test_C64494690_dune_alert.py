
import allure
from pages.device_management.base_page import DeviceManagementBasePage
from pages.device_management.alerts_page import AlertsPage


@allure.feature("Device Management")
@allure.story("Alert Subscription")
@allure.title("Quick Device Discovery and Full Alert Subscription")
def test_quick_device_discovery_by_ip(app):
    """
    Test: Discover device by IP and create alert subscription with all alerts
    """
    # Initialize page objects
    dm_page = DeviceManagementBasePage(app)
    alerts_page = AlertsPage(app)
    
    ip_address = "15.96.121.43"
    subscription_name = "HPW"

    with allure.step(f"Enter IP {ip_address} and click Go"):
        dm_page.enter_ip_and_click_go(ip_address)

    with allure.step("Handle Discovery Popup"):
        dm_page.handle_discovery_popup()

    with allure.step("Navigate to Alerts tab"):
        alerts_page.navigate_to_alerts_tab()

    with allure.step("Click Subscribe button"):
        alerts_page.click_subscribe_button()

    with allure.step(f"Complete alert subscription wizard with name: {subscription_name}"):
        alerts_page.complete_alert_subscription_wizard(subscription_name=subscription_name)
    
    allure.attach(
        f"Subscription '{subscription_name}' created successfully",
        name="Result",
        attachment_type=allure.attachment_type.TEXT
    )
    
    print(f"✔ Full Alert Subscription Workflow Completed Successfully for '{subscription_name}'")
