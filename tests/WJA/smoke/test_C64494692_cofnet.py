from pages.device_management.bconfig_page import ConfigurationPage
from pages.device_management.base_page import DeviceManagementBasePage


def test_select_device_and_configure_snmp(app):
    app = DeviceManagementBasePage(app)
    page = ConfigurationPage(app)

    app.enter_ip_and_click_go("15.96.121.43")
    app.handle_discovery_popup()

    page.click_config_tab()
    page.expand_network_tree()
    page.configure_system_contact()
    page.configure_system_name()
    

  
