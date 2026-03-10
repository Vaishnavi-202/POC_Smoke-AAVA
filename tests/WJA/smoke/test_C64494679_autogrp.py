import pytest
import allure
import time
from pages.device_management.group_page import GroupPage

@allure.title("WJA - Create Automatic Group using full wizard and delete it")
@allure.description(
    "Navigates to Groups, creates an Automatic Group using full wizard "
    "including details and properties, and finally deletes the group."
)
@pytest.mark.desktop
@pytest.mark.wja
def test_group_full_wizard_flow(app):

    group_name = "Auto_Test_Group"

    # Initialize the Page Object
    group_page = GroupPage(app)

    # 1️⃣ NAVIGATE TO GROUPS
    with allure.step("Open Overview → Groups"):
        group_page.open_overview_and_groups()

    # 2️⃣ START CREATE GROUP
    with allure.step("Click 'Create Group'"):
        group_page.click_create_group()

    # 3️⃣ ENTER GROUP NAME
    with allure.step(f"Enter group name: {group_name}"):
        group_page.enter_group_name(group_name)

    # 4️⃣ SELECT GROUP TYPE OPTIONS
    with allure.step("Select 'Automatic group' and enable properties checkbox"):
        group_page.select_group_type()

    # 5️⃣ NAVIGATE TO DETAILS SCREEN
    with allure.step("Click Next to reach details screen"):
        group_page.click_next()

    # 6️⃣ ADD FUNCTION DETAILS
    with allure.step("Add function details with value 'user'"):
        group_page.add_details()

    # 7️⃣ GO TO PROPERTIES SCREEN
    with allure.step("Click Next to reach properties screen"):
        group_page.click_next()

    # 8️⃣ ENTER DESCRIPTION
    with allure.step("Enter Description"):
        # Explicitly using the original method you requested
        group_page.enter_description_name("Auto group description")
    
    with allure.step("Click Next to proceed from Properties"):
        group_page.click_next()

    with allure.step("Click Next (if required) to reach Summary"):
        # Based on your original working code, there was a second Next click here
        group_page.click_next()

    # 9️⃣ CREATE GROUP
    with allure.step("Click 'Create Group'"):
        # Now we should be on the summary page where this button exists
        group_page.click_create()

    # 🔟 FINISH WIZARD
    with allure.step("Click 'Done' after group creation"):
        group_page.click_done()
        time.sleep(5)  # Allow UI to refresh

    # 1️⃣1️⃣ DELETE CREATED GROUP
    with allure.step("Select and delete created group"):
        group_page.select_group(group_name)
        group_page.delete_group()
