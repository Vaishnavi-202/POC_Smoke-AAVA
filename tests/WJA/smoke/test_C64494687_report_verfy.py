import pytest
import allure
import time
from pages.device_management.all_devices_page import AllDevicesPage
from pages.device_management.reports_page import ReportsPage
from pywinauto.keyboard import send_keys

@allure.title("Verify Device Utilization Data Collection")
@allure.description("""
1. Select device from All Devices
2. Navigate to Reports
3. Add device to Data Collection
4. Select Custom → Device Utilization by User
5. Complete wizard
6. Verify Collection Status
""")
def test_device_utilization_data_collection(app):

    all_devices_page = AllDevicesPage(app)
    reports_page = ReportsPage(app)

    printer_model = "HP LaserJet MFP M633"


    # 1️⃣ NAVIGATE TO ALL DEVICES
    with allure.step("Navigate to All Devices"):
        all_devices_page.click_all_devices()
        time.sleep(2) # Wait for grid to load

    # 2️⃣ SELECT DEVICE
    all_devices_page.select_device_by_model(printer_model)

    # Step 2: Open Reports tab
    reports_page.open_reports_tab()

    # Step 3: Add Devices
    reports_page.click_add_devices_to_data_collection()

    # Step 4: Select Custom Data Collection
    reports_page.select_custom_device_utilization()
    send_keys("{ENTER}")
    send_keys("{ENTER}")

    # Step 5: Wizard Navigation
    reports_page.go_through_wizard_till_confirm()
    reports_page.click_add_devices_and_done()

    # Step 6: Verify Status
    reports_page.open_reports_tab()

    reports_page.verify_collection_status_succeeded()


    
