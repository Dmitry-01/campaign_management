# User can't login because Analytics is blocked.
# import time
# import allure
# import pytest
#
# from pages.elements_page import CampaignManagementPage
# from pages.invite_user_page import TestInviteUsersPage
#
#
# @allure.feature("Test invite users")
# class TestInviteUsers:
#     @pytest.mark.order(12)
#     @allure.title("Checking invite client")
#     def test_invite_for_client(self, driver):
#         campaign_management_page = CampaignManagementPage(driver)
#         invite_user_page = TestInviteUsersPage(driver)
#         campaign_management_page.open_campaign()
#         campaign_management_page.go_to_the_first_item_folder()
#         campaign_management_page.go_to_the_first_campaign()
#         time.sleep(3)
#         invite_user_page.send_invite()
#         time.sleep(3)
#         link_for_registration = invite_user_page.get_mongo_data()
#         time.sleep(3)
#         campaign_management_page.open(link_for_registration)
#         time.sleep(3)
#         client_email = invite_user_page.fill_form_client_registration()
#         time.sleep(3)
#         name_campaign = invite_user_page.check_invite_campaign_name()
#
#         assert "Auto Campaign test " in name_campaign, "The client does not see the company "

    # User can't log in because Analytics is blocked.
    # Please be advised that the Company has ceased all operations effective October 1, 2023.
    # @pytest.mark.order(20)
    # @allure.title("Checking remove campaign client from campaign")
    # def test_no_access_to_campaign(self, driver):
    #     campaign_management_page = CampaignManagementPage(driver)
    #     invite_user_page = TestInviteUsersPage(driver)
    #
    #     campaign_management_page.open_campaign()
    #     campaign_management_page.go_to_the_first_item_folder()
    #     campaign_management_page.go_to_the_first_campaign()
    #     time.sleep(3)
    #     client_email,campaign_link = invite_user_page.get_client_email()
    #     invite_user_page.delete_user_from_campaign()
    #     time.sleep(3)
    #     invite_user_page.log_out()
    #     time.sleep(3)
    #     invite_user_page.client_log_in(client_email)
    #     time.sleep(3)
    #     invite_user_page.go_to_the_campaign_link(campaign_link)
    #     time.sleep(3)
    #     stub_text_1, stub_text_2 = invite_user_page.get_the_stub_text()
    #     assert stub_text_1 == "Sorry, it seems like you don’t have access to this section"
    #     assert stub_text_2 == "You can request access through campaign Owner or campaign Admin"
