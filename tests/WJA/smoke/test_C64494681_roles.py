import pytest
import allure
from pages.application_management.roles_page import RolesPage

@pytest.mark.desktop
@allure.feature("Role Management")
def test_create_and_assign_role(app):
    """Full flow to create a new role and assign it to a user"""
    
    # 1. Initialize Page (Base class handles module activation automatically)
    roles_page = RolesPage(app)

    # 2. Create new role using the high-level flow
    with allure.step("Create new role with all permissions"):
        # This one method replaces: click_roles_tree, right_roles, click_create, 
        # select_all_permissions, enter_role_name, click_create_role, and click_done.
        roles_page.create_new_role("USER")

    # 3. Assign the created role to a user
    with allure.step("Assign role to user"):
        # This one method replaces: click_users_tree, right_users, click_assign_role, 
        # click_add, add_user_window, click_close, and all 'Next/Done' steps.
        roles_page.assign_role_to_user(username="Users", domain="DESKTOP-UBBR6U3")