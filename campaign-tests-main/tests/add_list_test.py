import time
import allure
import pytest

from pages.add_list_page import AddListPage, AnalyticsListPage
from pages.elements_page import CampaignManagementPage


@allure.feature("Test add list into campaign")
class TestAddList:
    @pytest.mark.order(13)
    @allure.title("Checking add list")
    def test_add_list(self, driver):
        campaign_management_page = CampaignManagementPage(driver)
        add_list_page = AddListPage(driver)
        list_before = add_list_page.check_list_before_adding()
        print(f"Список который мы добавляем {list_before}")
        campaign_management_page.open_campaign()
        campaign_management_page.go_to_the_first_item_folder()
        campaign_management_page.go_to_the_first_campaign()
        time.sleep(1)
        add_list_page.add_list()
        time.sleep(3)
        driver.refresh()
        time.sleep(3)
        titles_list = add_list_page.check_add_list()
        print(titles_list)
        # expected_list = {'@khaby.lame', '@jlo', 'PewDiePie', "Pinkfong Baby Shark - Kids' Songs & Stories", '5-Minute Crafts', 'WWE', '✿ Kids Diana Show', 'Zee TV', 'HYBE LABELS', 'SET India', 'BANGTANTV', 'BLACKPINK', 'ChuChu TV Nursery Rhymes & Kids Songs', 'Tips Official', 'T-Series Bhakti Sagar', 'Zee Music Company', 'Canal KondZilla', 'Vlad and Niki', 'Goldmines', 'Sony SAB', 'Colors TV', 'Shemaroo Filmi Gaane', 'Justin Bieber'}
        # expected_list = {"T-Series", "MrBeast", "Cocomelon - Nursery Rhymes", "SET India", "✿ Kids Diana Show", "PewDiePie", "Like Nastya", "Vlad and Niki", "Zee Music Company", "WWE", "BLACKPINK", "Goldmines", "Sony SAB", "5-Minute Crafts", "BANGTANTV", "Zee TV", "HYBE LABELS", "Justin Bieber", "Pinkfong Baby Shark - Kids' Songs & Stories", "ChuChu TV Nursery Rhymes & Kids Songs", "ChuChu TV Nursery Rhymes & Kids Songs", "Colors TV", "Canal KondZilla", "Shemaroo Filmi Gaane", "T-Series Bhakti Sagar", "Tips Official"}
        # print(titles_list)
        for item in list_before:
            assert item in titles_list, f"Title '{item}' is no in list "

@allure.feature("Test create campaign from list")
class TestCreateCampaignFromList:
    @pytest.mark.order(22)
    @allure.title("Checking create campaign from List")
    def test_create_campaign_from_list(self, driver):
        analytics_list_page = AnalyticsListPage(driver)
        analytics_list_page.go_to_the_analytics_list_page()
        analytics_list_page.go_to_the_yt_list()
        list_name, list_influencers_titles = analytics_list_page.click_create_campaign_button()
        campaign_name, titles_influencers_in_the_campaign_list = analytics_list_page.check_campaign_name()
        time.sleep(3)
        assert campaign_name == f'Created from "{list_name}"'
        for item in list_influencers_titles:
            assert item in titles_influencers_in_the_campaign_list, f"Title '{item}' is no in list "