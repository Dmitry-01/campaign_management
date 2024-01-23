import time

from locators.add_list_locators import AddListLocators, AnalyticsListLocators
from pages.base_page import BasePage


class AddListPage(BasePage):
    locators = AddListLocators()
    def check_list_before_adding(self):
        self.element_is_visible(self.locators.LIST).click()
        self.element_is_visible(self.locators.LAST_LIST).click()
        all_titles = self.elements_are_present(self.locators.TITLES_LIST)
        # spent_list = []
        # for i in all_titles:
        #     spent_list.append(i)
        # print(spent_list)
        # for i in spent_list:
        #     print(i)
            # self.go_to_element(spent_list[i])
        all_titles_list = []
        for i in all_titles:
            title = i.text
            all_titles_list.append(title)
        return all_titles_list



    def add_list(self):
        self.element_is_visible(self.locators.ADD_LIST_BUTTON).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CHOOSE_LIST).click()
        time.sleep(3)
        self.element_is_visible(self.locators.ADD_LIST_MODAL_BUTTON).click()

    def check_add_list(self):
        titles_list = []
        all_titles = self.elements_are_present(self.locators.TITLE_CHANNEL)
        for item in all_titles:
            title = item.text
            titles_list.append(title)
        return titles_list


class AnalyticsListPage(BasePage):
    locators = AnalyticsListLocators()

    def go_to_the_analytics_list_page(self):
      self.element_is_visible(self.locators.LIST).click()


    def go_to_the_yt_list(self):
        self.element_is_visible(self.locators.YOUTUBE_LIST).click()

    def click_create_campaign_button(self):
        list_name_before = self.element_is_visible(self.locators.LIST_NAME).text
        list_influencers_titles_before = []
        all_influencers = self.elements_are_present(self.locators.ALL_INFLUENCERS)
        for i in all_influencers:
            list_influencers_titles_before.append(i.text)
        self.element_is_visible(self.locators.CREATE_CAMPAIGN_BUTTON).click()
        return list_name_before, list_influencers_titles_before

    def check_campaign_name(self):
        campaign_name = self.element_is_visible(self.locators.CAMPAIGN_NAME).text
        titles_influencers_in_the_campaign_list = []
        titles = self.elements_are_present(self.locators.TITLES)
        for i in titles:
            titles_influencers_in_the_campaign_list.append(i.text)
        return campaign_name, titles_influencers_in_the_campaign_list
