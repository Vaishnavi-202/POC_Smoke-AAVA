import time
 
from pywinauto.keyboard import send_keys
from pages.device_management.all_devices_page import AllDevicesPage
# from pages.device_management.configuratrion_page  import ConfigurationPage
 
def test_quick_discovery(app):
    devicesPage = AllDevicesPage(app)
    devicesPage.click_all_devices()

    ip_address = "15.96.121.135"

    devicesPage.enter_ip_and_click_go(ip_address)
    devicesPage.handle_discovery_popup()

    #devicesPage.click_first_device_row()
    devicesPage.click_config_tab()
    devicesPage.click_tree_item("My Settings")
    devicesPage.click_sub_tree_item("IPv4 Information")  
    devicesPage.click_sub_tree_item("System Location")  
    devicesPage.click_tree_item("My Settings")
 
    devicesPage.click_tree_item("Device")
    time.sleep(20)
    devicesPage.click_sub_tree_item("Asset Number") 
    devicesPage.click_tree_item("Device") 
 
 
    devicesPage.click_sub_tree_item("Web Services")  
    devicesPage.click_tree_item("ePrint Settings")










#     #----------------------------------------------------------

#     import time
# from pywinauto.keyboard import send_keys
# from pywinauto import timings

# # ✅ Inherit from your new Module Base Page
# from pages.device_management.base_page import DeviceManagementBasePage
# from conftest import ui_step_wait
# from config.logger import get_logger

# log = get_logger(__name__)

# class ConfigurationPage(DeviceManagementBasePage):

#     def click_all_devices(self):
#         """
#         Click the 'All Devices (x)' tree item
#         """
#         log.info("Clicking All Devices")
#         self.main_window.child_window(
#             title_re=r"All Devices.*",
#             control_type="TreeItem"
#         ).select()
#         ui_step_wait()
 
#     def perform_keyboard_actions(self):
#         log.info("Starting keyboard-only automation")
#         self.focus_window()
 
#         # TAB x3
#         for _ in range(1):
#             send_keys("{TAB}")
#             time.sleep(5)
 
#         send_keys("15.96.121.141")
#         time.sleep(5)
 
#         send_keys("{TAB}")
#         time.sleep(5)
 
#         send_keys("{ENTER}")
#         time.sleep(15)
 
#         send_keys("{ENTER}")
#         time.sleep(20)
 

    





 
 
 
