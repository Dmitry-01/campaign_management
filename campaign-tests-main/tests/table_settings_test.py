import time

import allure
import pytest

from pages.elements_page import CampaignManagementPage
from pages.table_settings_page import CustomColumn, ResetToDefaultPage, SwapTheColumnPage


@allure.feature("Test add custom column")
class TestAddColumn:
    @pytest.mark.order(15)
    @allure.title("Checking custom add column into table")
    def test_add_column_into_table(self, driver):
        campaign_management_page = CampaignManagementPage(driver)
        custom_column = CustomColumn(driver)
        campaign_management_page.open_campaign()
        campaign_management_page.go_to_the_first_item_folder()
        campaign_management_page.go_to_the_first_campaign()
        custom_column.add_custom_column()
        column_titles_list = custom_column.check_add_custom_column()
        assert "Custom field Text" in column_titles_list

@allure.feature("Test reset default")
class TestResetDefault:
    @pytest.mark.order(16)
    @allure.title("Checking custom add column into table")
    def test_reset_to_defaults_column(self, driver):
        campaign_management_page = CampaignManagementPage(driver)
        table_settings_page = ResetToDefaultPage(driver)
        campaign_management_page.open_campaign()
        campaign_management_page.go_to_the_first_item_folder()
        campaign_management_page.go_to_the_first_campaign()
        column_list_before = table_settings_page.check_column_list_before()
        table_settings_page.click_on_the_reset()
        column_list_after = table_settings_page.check_column_list_after()
        assert column_list_before != column_list_after, "The columns haven't changed"

@allure.feature("Test swap column")
class TestChangeColumn:
    @pytest.mark.order(21)
    @allure.title("Checking change the columns")
    def test_change_column(self, driver):
        change_column_page = SwapTheColumnPage(driver)
        campaign_management_page = CampaignManagementPage(driver)
        campaign_management_page.open_campaign()
        campaign_management_page.go_to_the_first_item_folder()
        campaign_management_page.go_to_the_first_campaign()
        column_before, column_after = change_column_page.change_column()
        assert column_before != column_after, "The columns haven't changed"

