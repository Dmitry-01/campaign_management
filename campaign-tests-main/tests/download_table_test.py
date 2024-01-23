# import allure
# import pytest
#
# from pages.download_table_page import DownloadTablePage
# from pages.elements_page import CampaignManagementPage
#
#
# @allure.feature("Test download table")
# class TestDownloadTable:
#     @pytest.mark.order(14)
#     @allure.title("Checking download table")
#     def test_download_table(self, driver):
#         campaign_management_page = CampaignManagementPage(driver)
#         download_table = DownloadTablePage(driver)
#         campaign_management_page.open_campaign()
#         campaign_management_page.go_to_the_first_item_folder()
#         campaign_management_page.go_to_the_first_campaign()
#         campaign_title = download_table.download_table()
#         check = download_table.check_download_file(campaign_title)
#         assert check is True, "the file has not been downloaded"