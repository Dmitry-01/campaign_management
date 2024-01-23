import time
import allure
import pytest

from pages.add_influencers_and_content_page import AddInfluencersAndContentPage, TableCampaignPage
from pages.elements_page import CampaignManagementPage


@allure.suite("Table manipulation (add channel, video. Fill in table)")
class TestTables:
    @allure.feature("Test add influencers And content")
    class TestAddInfluencersAndContent:
        @pytest.mark.order(7)
        @allure.title("Check channel adding ")
        def test_add_influencers(self, driver):

            campaign_management_page = CampaignManagementPage(driver)
            add_influencers_and_content_page = AddInfluencersAndContentPage(driver)
            campaign_management_page.open_campaign()
            campaign_management_page.go_to_the_first_item_folder()
            campaign_management_page.go_to_the_first_campaign()
            time.sleep(3)
            add_influencers_and_content_page.add_influencers()
            time.sleep(1)
            username_list = add_influencers_and_content_page.search_influencer_list()
            print(username_list)
            time.sleep(3)
            assert "PewDiePie" in username_list, "This channel is absent "
            assert "@khaby.lame" in username_list, "This channel is absent "
            # Instagram is blocked
            # assert "@jlo" in username_list, "This channel is absent "

        # @pytest.mark.order(8)
        # @allure.title("Checking the opening of a channel in social network")
        # def test_open_social_media_influencers(self, driver):
        #     campaign_management_page = CampaignManagementPage(driver)
        #     add_influencers_and_content_page = AddInfluencersAndContentPage(driver)
        #
        #     campaign_management_page.open_campaign()
        #     campaign_management_page.go_to_the_first_item_folder()
        #     campaign_management_page.go_to_the_first_campaign()
        #     time.sleep(1)
        #     list_for_check_title = add_influencers_and_content_page.go_to_social_media()
        #     time.sleep(1)
        #     assert 'khaby.lame' in  list_for_check_title
        #     # Instagram is blocked
        #     # assert 'jlo' in  list_for_check_title
        #     assert '@PewDiePie' in  list_for_check_title

        @pytest.mark.order(9)
        @allure.title("Checking fill influencers table")
        def test_fill_influencers_table(self, driver):
            campaign_management_page = CampaignManagementPage(driver)
            table_campaign_page = TableCampaignPage(driver)
            campaign_management_page.open_campaign()
            campaign_management_page.go_to_the_first_item_folder()
            campaign_management_page.go_to_the_first_campaign()
            time.sleep(1)
            table_campaign_page.clear_all_fields()
            table_campaign_page.change_column_select()
            table_campaign_page.change_editable_field_influencers()
            list_for_check = table_campaign_page.check_field_influencers_table()
            list_for_check_select = table_campaign_page.check_select_influencers_table()
            print(f"list_for_check: {list_for_check_select}")
            assert 'Today' in list_for_check, "The date has not changed"
            assert '111' in list_for_check, "The AVG Views has not changed"
            assert '80%' in list_for_check, "The EXP ER has not changed"
            assert '$1 500' in list_for_check, "The Price has not changed"
            assert 'Auto test Remarks' in list_for_check, "The Remarks has not changed"
            assert 'Auto test Client Remarks' in list_for_check, "The Client Remarks has not changed"
            assert 'New' in list_for_check_select, "The Status has not changed"
            assert 'Pre-roll' in list_for_check_select, "The Format has not changed"
            assert 'Andorra' in list_for_check_select, "The country has not changed"
            assert 'Abkhazian' in list_for_check_select, "The language has not changed"
            assert "BuzzGuru Admin 2" in list_for_check_select, "The Manger has not changed"
            assert "Gaming" in list_for_check_select, "The Category has not changed"

        @pytest.mark.order(10)
        @allure.title("Checking adding video")
        def test_add_video(self, driver):
            campaign_management_page = CampaignManagementPage(driver)
            add_influencers_and_content_page = AddInfluencersAndContentPage(driver)
            campaign_management_page.open_campaign()
            campaign_management_page.go_to_the_first_item_folder()
            campaign_management_page.go_to_the_first_campaign()
            time.sleep(3)
            add_influencers_and_content_page.go_to_the_content_page()
            time.sleep(3)
            add_influencers_and_content_page.add_content()
            video_title = add_influencers_and_content_page.search_influencer_video()
            assert "They rejected my..." in video_title, "This video is absent "
            # Instagram is blocked
            # assert "Очумелые ручки! За 2 минуты..." in video_title, "This video is absent "
            assert "Дорогая Грузия. Что нас..." in video_title, "This video is absent "

        @pytest.mark.order(11)
        @allure.title("Checking fill content table")
        def test_fill_content_table(self, driver):
            campaign_management_page = CampaignManagementPage(driver)
            table_campaign_page = TableCampaignPage(driver)
            add_influencers_and_content_page = AddInfluencersAndContentPage(driver)
            campaign_management_page.open_campaign()
            campaign_management_page.go_to_the_first_item_folder()
            campaign_management_page.go_to_the_first_campaign()
            time.sleep(3)
            add_influencers_and_content_page.go_to_the_content_page()
            time.sleep(1)
            table_campaign_page.clear_all_fields_content()
            table_campaign_page.change_editable_field_content()
            time.sleep(1)
            list_for_check = table_campaign_page.check_field_content_table()
            print(list_for_check)
            assert '$42.23' in list_for_check
            assert '765.43' in list_for_check
            assert '2 000' in list_for_check
            assert '434.3' in list_for_check
            assert '532.23' in list_for_check
            assert '$111.23' in list_for_check
            assert 'Lorem ipsum dolor sit amet, consectetur Remark' in list_for_check
            assert 'Lorem ipsum dolor sit amet, consectetur Client Remark' in list_for_check
            assert '323.34' in list_for_check

