import allure

from locators.elements_page_locators import CampaignManagerLocators
from pages.base_page import BasePage
import time

n = str(time.time())


class CampaignManagementPage(BasePage):
    locators = CampaignManagerLocators()

    def home_page(self):
        return self.element_is_visible(self.locators.HEADER_TEXT).text

    def open_campaign(self):
        self.element_is_visible(self.locators.CAMPAIGN_MANAGER).click()

    def open_demo_campaign(self):
        self.go_to_element(self.locators.CLICK_DEMO_CAMPAIGN).click()

    def demo_campaign_is_visiable(self):
        self.go_to_element(self.locators.DEMO_CAMPAIGN).click()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.EMAIL).send_keys('d.serakov+testing@buzzguru.com')
        self.element_is_visible(self.locators.PASSWORD).send_keys('d.serakov+testing@buzzguru.com')
        self.element_is_visible(self.locators.SUBMIT).click()

    def check_demo_campaign_is_open(self):
        text_demo_campaign = self.element_is_visible(self.locators.DEMO_CAMPAIGN).text
        return text_demo_campaign

    def create_folder(self):
        self.element_is_visible(self.locators.ADD_FOLDER_BUTTON).click()
        self.element_is_visible(self.locators.FOLDER_NAME).clear()
        self.element_is_visible(self.locators.FOLDER_NAME).send_keys(' Auto Test Created Folder ')
        self.element_is_visible(self.locators.FOLDER_DESCRIPTION).send_keys('Auto Description for Folder Automation')
        self.element_is_visible(self.locators.NEXT_BUTTON).click()
        self.element_is_visible(self.locators.CREATE_FOLDER_BUTTON).click()

    def get_folder_name(self):
        folder = self.element_is_visible(self.locators.TEXT_FOLDER_NAME).text
        return folder

    def get_description(self):
        description = self.element_is_visible(self.locators.TEXT_FOLDER_DESCRIPTION).text
        return description

    def go_to_the_first_item_folder(self):
        self.element_is_present(self.locators.FIRTS_TEST_FOLDER).click()
        time.sleep(3)

    def open_test_folder_settings(self):
        self.element_is_visible(self.locators.FIRTS_TEST_FOLDER).click()
        self.element_is_visible(self.locators.BUTTON_SETTINGS).click()
        self.element_is_visible(self.locators.FOLDER_SETTINGS).click()

    def change_and_save_name_description_folder(self):
        self.element_is_visible(self.locators.FOLDER_NAME).click()
        self.element_is_visible(self.locators.FOLDER_NAME).clear()
        self.element_is_visible(self.locators.FOLDER_NAME).send_keys('Auto Folder name 12345')

        self.element_is_visible(self.locators.FOLDER_DESCRIPTION).click()
        self.element_is_visible(self.locators.FOLDER_DESCRIPTION).clear()
        self.element_is_visible(self.locators.FOLDER_DESCRIPTION).send_keys('Auto Folder description 12345')

        self.element_is_visible(self.locators.SAVE_BUTTON).click()

    def go_to_campaign_manager_page(self):
        self.element_is_visible(self.locators.CAMPAIGN_MANAGER).click()

    def click_to_the_delete_folder_button(self):
        self.element_is_visible(self.locators.FOLDER_BUTTON_SETTINGS).click()
        self.element_is_visible(self.locators.FOLDER_BUTTON_DELETED).click()

    def check_popup_delete_folder(self):
        return self.element_is_visible(self.locators.POPUP_DELETE_FOLDER).text

    def click_to_the_delete_folder_button_inside_folder(self):
        self.element_is_visible(self.locators.BUTTON_SETTINGS).click()
        self.element_is_visible(self.locators.DELETE_FOLDER).click()

    # Create campaign

    def click_to_the_create_campaign_button(self):
        self.element_is_visible(self.locators.CREATE_CAMPAIGN_BUTTON).click()

    def fill_all_fields_campaign(self):
        self.element_is_visible(self.locators.INPUT_CAMPAIGN_NAME).clear()
        self.element_is_visible(self.locators.INPUT_CAMPAIGN_NAME).send_keys(f"Auto Campaign test {n}")

        self.element_is_visible(self.locators.INPUT_CAMPAIGN_DATES).click()
        all_date = self.elements_are_visible(self.locators.All_VALUE_DATE)
        first_date = all_date[0].click()
        second_date = all_date[28].click()
        self.element_is_visible(self.locators.INPUT_CAMPAIGN_DATES).click()

        # Campaign_page
        self.element_is_visible(self.locators.INPUT_PLANNED_BUDGET).send_keys("1000")
        self.element_is_visible(self.locators.INPUT_TOTAL_VIEWS).send_keys("1000")
        self.element_is_visible(self.locators.INPUT_EXPECTED_CPM).send_keys("1000")
        self.element_is_visible(self.locators.INPUT_EXPECTED_CPC).send_keys("1000")
        self.element_is_visible(self.locators.INPUT_CAMPAIGN_DESCRIPTION).send_keys(
            f"It is description for test campaign{n}")
        self.element_is_visible(self.locators.BUTTON_NEXT).click()

        # Requirements page
        self.element_is_visible(self.locators.SELECT_GEO).click()
        all_country_check_box = self.elements_are_visible(self.locators.CHECK_BOX_ALL_COUNTRY)
        first_check = all_country_check_box[0].click()
        self.element_is_visible(self.locators.CLICK_GEO_AGAIN).click()

        self.element_is_visible(self.locators.AGES).click()
        all_country_check_box = self.elements_are_visible(self.locators.ALL_AGES_CHECK_BOX)
        all_country_check_box[0].click()
        time.sleep(1)

        self.element_is_visible(self.locators.PLATFORMS).click()
        all_platforms = self.elements_are_visible(self.locators.ALL_PLATFORMS)
        all_platforms[0].click()
        self.element_is_visible(self.locators.CLOSE_PLATFORMS_DROPDOWN).click()
        time.sleep(1)

        self.element_is_visible(self.locators.CATEGORY).click()
        all_category = self.elements_are_visible(self.locators.ALL_CATEGORY)
        all_category[0].click()
        self.element_is_visible(self.locators.CLOSE_CATGORY_DROPDOWN).click()
        time.sleep(1)

        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        time.sleep(3)

        # Status page
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        time.sleep(3)

        # Client decision page
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        time.sleep(3)

        # Format page
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        time.sleep(3)

        # Team page
        create_cmpaign_button = self.element_is_visible(self.locators.CREATE_CAMPAIGN_BUTTON_TEAM_PAGE)
        self.go_to_element(create_cmpaign_button)
        self.element_is_visible(self.locators.CREATE_CAMPAIGN_BUTTON_TEAM_PAGE).click()
        time.sleep(3)

    def check_campaign_name_inside_campign(self):
        return self.element_is_visible(self.locators.CAMPAIGN_NAME_INSIDE_CAMPAIGN_TEXT).text

    def check_campaign_name(self):
        campaign_name = []
        campaign_name_title = self.elements_are_present(self.locators.CAMPAIGN_NAME_SPISOK_KOMPANII_TEXT)
        for item in campaign_name_title:
            title = item.text
            campaign_name.append(title)
        return campaign_name
        # return self.element_is_visible(self.locators.CAMPAIGN_NAME_SPISOK_KOMPANII_TEXT).text

    def go_to_the_first_campaign(self):
        with allure.step("Go to the first campaign"):
            self.element_is_visible(self.locators.FIRST_CAMPAIGN).click()

    # def click_delete_campaign(self):
    #     all_campaigns_settings_button = self.elements_are_present(self.locators.ALL_CAMPAIGNS_SETTINGS_BUTTON)
    #     self.element_is_visible(self.locators.DELETE_CAMPAIGN_BUTTON).click()
    #     for i in
