import allure
from pages.device_management.template_verify import TemplateVerifyPage


@allure.feature("WJA Template Application")
@allure.story("Apply Control Panel Display (Default) template")
def test_apply_template_flow(app):

    page = TemplateVerifyPage(app)

    with allure.step("Focus main window"):
        page.focus_window()

    with allure.step("Open Configuration → Templates"):
        page.open_configuration_and_templates()

    with allure.step("Select Control Panel Display (Default)"):
        page.select_control_panel_default()

    with allure.step("Click Apply"):
        page.click_apply()

    with allure.step("Click Next"):
        page.click_next()

    with allure.step("Navigate to Band 0 row 1 (TAB + DOWN)"):
        page.wizard_tab_down_to_band0()

    with allure.step("Move Device Model using >"):
        page.click_move_right()

    with allure.step("Click Next"):
        page.click_next()

    with allure.step("Click Apply Template"):
        page.click_apply_template()

    with allure.step("Finish with Done"):
        page.click_done()

    with allure.step("Open History"):
        page.open_history()

    with allure.step("Select Band 0 row 1"):
        page.select_band0_row1()
