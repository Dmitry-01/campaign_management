import time
import allure
import pytest

from pages.elements_page import CampaignManagementPage

@allure.suite("Campaign management")
class TestElements:
    @allure.feature("Test create campaign and folder, opening demo campaign")
    class TestCampaignManager:
        #simple test for check headless option
        # def test_simple_headless(self, driver):
        #     campaign_management_page = CampaignManagementPage(driver)
        #     home_page_header_text = campaign_management_page.home_page()
        #     print(home_page_header_text)
        #     assert home_page_header_text == "Level up your next influencer marketing campaign!"
        # Проверка открытия Demo папки
        @pytest.mark.order(1)
        @allure.title("Checking the opening of a demo campaign")
        def test_open_demo_campaign(self, driver):
            campaign_management_page = CampaignManagementPage(driver)
            campaign_management_page.open_campaign()
            # driver.get('https://testing.buzz.guru/campaigns/62d93d77de40c2002086a905')
            driver.get('https://staging.buzz.guru/campaigns/62e2ad2b072f1a001afaf827')

            time.sleep(3)
            text_demo_campaign = campaign_management_page.check_demo_campaign_is_open()
            assert text_demo_campaign == 'Demo Campaign - Archived', 'There is no such company.'
        #
        @pytest.mark.order(2)
        @allure.title("Checking creating folder")
        def test_create_folder(self, driver):
            campaign_management_page = CampaignManagementPage(driver)
            campaign_management_page.open_campaign()
            campaign_management_page.create_folder()
            text_folder_name = campaign_management_page.get_folder_name()
            text_description_name = campaign_management_page.get_description()
            time.sleep(3)
            assert text_folder_name == 'Auto Test Created Folder'
            assert text_description_name == 'Auto Description for Folder Automation'
        #
        @pytest.mark.order(3)
        @allure.title("Checking for changes to the folder name and description")
        def test_change_folder_name_and_description(self, driver):
            time.sleep(3)
            campaign_management_page = CampaignManagementPage(driver)
            campaign_management_page.open_campaign()
            campaign_management_page.open_test_folder_settings()
            campaign_management_page.change_and_save_name_description_folder()
            campaign_management_page.go_to_campaign_manager_page()
            campaign_management_page.go_to_the_first_item_folder()
            rename_folder_name = campaign_management_page.get_folder_name()
            rename_description_name = campaign_management_page.get_description()
            assert rename_folder_name == 'Auto Folder name 12345'
            assert rename_description_name == 'Auto Folder description 12345'
        #
        @pytest.mark.order(4)
        @allure.title("Checking pop up when deleting folder")
        def test_pop_up_when_delete_folder(self, driver):

            campaign_management_page = CampaignManagementPage(driver)
            campaign_management_page.open_campaign()
            time.sleep(3)
            campaign_management_page.click_to_the_delete_folder_button()
            popup_message = campaign_management_page.check_popup_delete_folder()
            assert popup_message in "The folder cannot be restored, although the campaigns inside will remain in your workspace"
        #
        @pytest.mark.order(5)
        @allure.title("Checking pop up when deleting folder inside folder")
        def test_popup_when_delete_folder_inside_folder(self, driver):
            campaign_management_page = CampaignManagementPage(driver)
            campaign_management_page.open_campaign()
            campaign_management_page.go_to_the_first_item_folder()
            campaign_management_page.click_to_the_delete_folder_button_inside_folder()
            popup_message_inside_folder = campaign_management_page.check_popup_delete_folder()
            assert popup_message_inside_folder in "The folder cannot be restored, although the campaigns inside will remain in your workspace"
        #
        @pytest.mark.order(6)
        @allure.title("Checking creating campaign")
        def test_create_campaign(self, driver):
            campaign_management_page = CampaignManagementPage(driver)
            campaign_management_page.open_campaign()
            campaign_management_page.go_to_the_first_item_folder()
            campaign_management_page.click_to_the_create_campaign_button()
            campaign_management_page.fill_all_fields_campaign()
            input_campaign_name_text = campaign_management_page.check_campaign_name_inside_campign()
            time.sleep(3)
            campaign_management_page.open_campaign()
            campaign_management_page.go_to_the_first_item_folder()
            time.sleep(3)
            campaign_name_text = campaign_management_page.check_campaign_name()
            assert input_campaign_name_text in campaign_name_text, "There is no such company"

        # @pytest.mark.order(23)
        # @allure.title("Checking creating campaign")
        # def test_delete_campaign_from_folder(self, driver):
        #     campaign_management_page = CampaignManagementPage(driver)
        #     campaign_management_page.open_campaign()
        #     campaign_management_page.go_to_the_first_item_folder()
        #     campaign_management_page.click_delete_campaign()
        #     time.sleep(10)