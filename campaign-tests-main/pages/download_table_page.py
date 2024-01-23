import os
import time

from locators.download_table_locators import DownloadTablePageLocators
from pages.base_page import BasePage


class DownloadTablePage(BasePage):
    locators = DownloadTablePageLocators()

    def download_table(self):
        time.sleep(3)
        self.element_is_visible(self.locators.BUTTONS_TABLE_DOWMLOAD).click()
        time.sleep(1)
        campaign_title = self.element_is_present(self.locators.TITLE_CAMPAIGN).text
        time.sleep(1)
        self.element_is_visible(self.locators.EXPORT_BUTTON).click()
        time.sleep(1)
        return campaign_title

    def check_download_file(self, campaign_title):
        path_name_file = rf'/Users/Dmitry/Downloads/{campaign_title}.csv'
        check_file = os.path.exists(path_name_file)
        os.remove(path_name_file)
        return check_file