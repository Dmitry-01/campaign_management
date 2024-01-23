from selenium.webdriver import Keys

from data.data import *
from locators.add_influencers_and_content_locators import AddInfluencersAndContentLocators
from locators.elements_page_locators import TableCampaignPageLocators
from pages.base_page import BasePage


class AddInfluencersAndContentPage(BasePage):
    locators = AddInfluencersAndContentLocators()

    def add_influencers(self):
        for item in channel_list:
            self.element_is_visible(self.locators.ADD_INFLUENCER_BUTTON).click()
            self.element_is_visible(self.locators.INPUT_ENTER_LINK).send_keys(item)
            self.element_is_visible(self.locators.ADD_INFLUENCER_BUTTON).click()

    def search_influencer_list(self):
        username_list = self.elements_are_present(self.locators.SEARCH_CHANNEL)
        data = []
        for item in username_list:
            time.sleep(1)
            data.append(item.text)
        time.sleep(1)
        return data

    def go_to_the_content_page(self):
        self.element_is_visible(self.locators.CONTENT_TAB).click()

    def add_content(self):
        # add youtube video
        self.element_is_visible(self.locators.ADD_CONTENT_BUTTON).click()
        self.element_is_visible(self.locators.INPUT_LINK).send_keys(youtube_video)
        self.element_is_visible(self.locators.CONTENT_ADD_BUTTON_MODAL).click()
        #Instagram is blocked
        # add instagram posts
        # self.element_is_visible(self.locators.ADD_CONTENT_BUTTON).click()
        # self.element_is_visible(self.locators.INSTAGRAM_TAB).click()
        # self.element_is_visible(self.locators.INPUT_LINK).send_keys(instagram_post)
        # self.element_is_visible(self.locators.CONTENT_ADD_BUTTON_MODAL).click()
        time.sleep(3)
        # add tiktok posts
        self.element_is_visible(self.locators.ADD_CONTENT_BUTTON).click()
        self.element_is_visible(self.locators.TIKTOK_TAB).click()
        self.element_is_visible(self.locators.INPUT_LINK).send_keys(tiktok_post)
        self.element_is_visible(self.locators.CONTENT_ADD_BUTTON_MODAL).click()
        time.sleep(3)

    def search_influencer_video(self):
        username_video_list = self.elements_are_visible(self.locators.VIDEO_SEARCH_CHANNEL)
        data_video = []
        for item in username_video_list:
            data_video.append(item.text)
        time.sleep(5)
        return data_video

    def go_to_social_media(self):
        social_media_buttons = self.elements_are_visible(self.locators.ALL_SOCIAL_MEDIA_BUTTONS)
        list_social_media_button = []
        list_for_check_title = []
        # Instagram is blocked
        # locators_list = [self.locators.TIKTOK_CHANNEL_TITLE, self.locators.INSTAGRAM_CHANNEL_TITLE,
        #                  self.locators.YOUTUBE_CHANNEL_TITLE]
        locators_list = [self.locators.TIKTOK_CHANNEL_TITLE, self.locators.YOUTUBE_CHANNEL_TITLE]

        for item in social_media_buttons:
            list_social_media_button.append(item)

        for item in range(len(list_social_media_button[:3])):
            time.sleep(1)
            self.switch_to_window(0)
            list_social_media_button[item].click()
            self.switch_to_window(item + 1)
            titles = self.element_is_present(locators_list[item]).text
            list_for_check_title.append(titles)
        return list_for_check_title

class TableCampaignPage(BasePage):
    locators = TableCampaignPageLocators()

    def clear_all_fields(self):
        point_button = self.elements_are_visible(self.locators.POINT_BUTTON)
        for item in point_button:
            self.go_to_element(item)
            item.click()
            two_button_list = []
            two_button = self.elements_are_visible(self.locators.TWO_BUTTONS)
            for i in two_button:
                two_button_list.append(i)
            two_button_list[1].click()
            self.element_is_visible(self.locators.CLEAR_BUTTON).click()

    def change_column_select(self):

        # Заполнение селектов
        all_select_columns = self.elements_are_visible(self.locators.ALL_SELECT_COLUMNS)
        list_select_column = []
        for item in all_select_columns:
            list_select_column.append(item)

        for item in range(len(list_select_column)):
            self.go_to_element(list_select_column[item])
            time.sleep(1)
            list_select_column[item].click()
            time.sleep(1)
            self.element_is_visible(self.locators.INPUT_SELECT_STATUS).send_keys(Keys.ARROW_DOWN)
            self.element_is_visible(self.locators.INPUT_SELECT_STATUS).send_keys(Keys.ENTER)
            time.sleep(1)

    # Заполнение остальных полей
    def change_editable_field_influencers(self):
        all_edite_columns_influencers_table = self.elements_are_visible(self.locators.ALL_EDITEVALUE_COLUMNS)

        date_list = []
        avg_views_list = []
        exp_er_list = []
        price_list = []
        remarks = []
        client_remarks = []

        for item in all_edite_columns_influencers_table:
            var = item.text
            if var == "Set date":
                date_list.append(item)
            elif var == "Set average views":
                avg_views_list.append(item)
            elif var == "Set Expected ER":
                exp_er_list.append(item)
            elif var == "Set price":
                price_list.append(item)
            elif var == "Add comments":
                remarks.append(item)
            elif var == "Add a client comment":
                client_remarks.append(item)

        for i in range(len(date_list)):
            self.go_to_element(date_list[i])
            time.sleep(1)
            date_list[i].click()
            self.element_is_visible(self.locators.INFLUENCERS_TUB).click()

        for i in range(len(avg_views_list)):
            self.go_to_element(avg_views_list[i])
            time.sleep(1)
            avg_views_list[i].click()
            self.element_is_visible(self.locators.AVG_VIEW).send_keys("111")
            self.element_is_visible(self.locators.INFLUENCERS_TUB).click()

        for i in range(len(exp_er_list)):
            self.go_to_element(exp_er_list[i])
            time.sleep(1)
            exp_er_list[i].click()
            self.element_is_visible(self.locators.EXP_ER).send_keys("80")
            self.element_is_visible(self.locators.INFLUENCERS_TUB).click()

        for i in range(len(price_list)):
            self.go_to_element(price_list[i])
            time.sleep(1)
            price_list[i].click()
            self.element_is_visible(self.locators.PRICE).send_keys("1500")
            self.element_is_visible(self.locators.INFLUENCERS_TUB).click()

        for i in range(len(remarks)):
            self.go_to_element(remarks[i])
            time.sleep(1)
            remarks[i].click()
            self.element_is_visible(self.locators.REMARKS).send_keys("Auto test Remarks")
            self.element_is_visible(self.locators.INFLUENCERS_TUB).click()

        for i in range(len(client_remarks)):
            self.go_to_element(client_remarks[i])
            time.sleep(1)
            client_remarks[i].click()
            self.element_is_visible(self.locators.REMARKS).send_keys("Auto test Client Remarks")
            self.element_is_visible(self.locators.INFLUENCERS_TUB).click()

    def change_editable_field_content(self):
        all_edite_columns_content_table = self.elements_are_visible(self.locators.ALL_EDITEVALUE_COLUMNS)
        other_editable_value_content_table = self.elements_are_visible(self.locators.OTHER_EDITABLE_VALUE_CONTENT_TABLE)

        spent_list = []
        views_list = []
        reach_list = []
        shares_list = []
        saves_list = []
        interactions_list = []
        clicks_list = []
        installs_list = []
        registrations_list = []
        depsits_list = []
        actions_list = []
        revenue_test = []
        remarks_list = []
        client_remarks_list = []

        for item in all_edite_columns_content_table:
            var = item.text
            if var == "Set total spent":
                spent_list.append(item)
            elif var == "Set total clicks":
                clicks_list.append(item)
            elif var == "Set total installs":
                installs_list.append(item)
            elif var == "Set total registrations":
                registrations_list.append(item)
            elif var == "Set total deposits":
                depsits_list.append(item)
            elif var == "Set total actions":
                actions_list.append(item)
            elif var == "Set total revenue":
                revenue_test.append(item)
            elif var == "Add comments":
                remarks_list.append(item)
            elif var == "Add a client comment":
                client_remarks_list.append(item)

        for item in other_editable_value_content_table:
            var = item.text
            if var == "Set total views":
                views_list.append(item)
            elif var == "Set total reach":
                reach_list.append(item)
            elif var == "Set total shares":
                shares_list.append(item)
            elif var == "Set total saves":
                saves_list.append(item)
            elif var == "Set total interactions":
                interactions_list.append(item)

        for i in range(len(spent_list)):
            self.go_to_element(spent_list[i])
            time.sleep(1)
            spent_list[i].click()
            self.element_is_visible(self.locators.SPENT).send_keys("42.23")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(views_list)):
            self.go_to_element(views_list[i])
            time.sleep(1)
            views_list[i].click()
            self.element_is_visible(self.locators.VIEWS).send_keys("99325.43")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(reach_list)):
            self.go_to_element(reach_list[i])
            time.sleep(1)
            reach_list[i].click()
            self.element_is_visible(self.locators.REACH).send_keys("3575.42")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(shares_list)):
            self.go_to_element(shares_list[i])
            time.sleep(1)
            shares_list[i].click()
            self.element_is_visible(self.locators.SHARES).send_keys("1445.54")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(saves_list)):
            self.go_to_element(saves_list[i])
            time.sleep(1)
            saves_list[i].click()
            self.element_is_visible(self.locators.SAVES).send_keys("323.34")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(interactions_list)):
            self.go_to_element(interactions_list[i])
            time.sleep(1)
            interactions_list[i].click()
            self.element_is_visible(self.locators.INTER).send_keys("9399.45")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(clicks_list)):
            self.go_to_element(clicks_list[i])
            time.sleep(1)
            clicks_list[i].click()
            self.element_is_visible(self.locators.CLICKS).send_keys("765.43")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(installs_list)):
            self.go_to_element(installs_list[i])
            time.sleep(1)
            installs_list[i].click()
            self.element_is_visible(self.locators.INSTALL).send_keys("3422332")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(registrations_list)):
            self.go_to_element(registrations_list[i])
            time.sleep(1)
            registrations_list[i].click()
            self.element_is_visible(self.locators.REGISTRATION).send_keys("2000")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(depsits_list)):
            self.go_to_element(depsits_list[i])
            time.sleep(1)
            depsits_list[i].click()
            self.element_is_visible(self.locators.DEPOSITS).send_keys("434.3")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(actions_list)):
            self.go_to_element(actions_list[i])
            time.sleep(1)
            actions_list[i].click()
            self.element_is_visible(self.locators.ACTION).send_keys("532.23")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(revenue_test)):
            self.go_to_element(revenue_test[i])
            time.sleep(1)
            revenue_test[i].click()
            self.element_is_visible(self.locators.REVENUE).send_keys("111.23")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(remarks_list)):
            self.go_to_element(remarks_list[i])
            time.sleep(1)
            remarks_list[i].click()
            self.element_is_visible(self.locators.REMARKS).send_keys("Lorem ipsum dolor sit amet, consectetur Remark")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(client_remarks_list)):
            self.go_to_element(client_remarks_list[i])
            time.sleep(1)
            client_remarks_list[i].click()
            self.element_is_visible(self.locators.REMARKS).send_keys(
                "Lorem ipsum dolor sit amet, consectetur Client Remark")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

    def check_field_content_table(self):

        all_edite_columns_content_table_after = self.elements_are_present(self.locators.ALL_EDITEVALUE_COLUMNS_AFTER)
        other_editable_value_content_table_after = self.elements_are_present(
            self.locators.OTHER_EDITABLE_VALUE_CONTENT_TABLE_AFTER)

        list_for_check = []

        for item in all_edite_columns_content_table_after:
            var = item.text
            list_for_check.append(var)

        for item in other_editable_value_content_table_after:
            var = item.text
            list_for_check.append(var)

        return list_for_check

    def check_field_influencers_table(self):
        all_edite_columns = self.elements_are_visible(self.locators.CHECK_ALL_EDITEVALUE_COLUMNS)
        list_for_check = []
        for item in all_edite_columns:
            var = item.text
            list_for_check.append(var)
        return list_for_check

class TableCampaignPage(BasePage):
    locators = TableCampaignPageLocators()

    # Очистка всех полей. Вкладка Influencers
    def clear_all_fields(self):

        point_button = self.elements_are_visible(self.locators.POINT_BUTTON)
        for item in point_button:
            self.go_to_element(item)
            item.click()
            two_button_list = []
            two_button = self.elements_are_visible(self.locators.TWO_BUTTONS)
            for i in two_button:
                two_button_list.append(i)
            two_button_list[2].click()
            self.element_is_visible(self.locators.CLEAR_BUTTON).click()

    # Очистка всех полей. Вкладка Content
    def clear_all_fields_content(self):

        point_button = self.elements_are_visible(self.locators.POINT_BUTTON)
        for item in point_button:
            self.go_to_element(item)
            item.click()
            two_button_list = []
            two_button = self.elements_are_visible(self.locators.TWO_BUTTONS)
            for i in two_button:
                two_button_list.append(i)
            two_button_list[1].click()
            self.element_is_visible(self.locators.CLEAR_BUTTON).click()

    def change_column_select(self):

        # Заполнение селектов
        all_select_columns = self.elements_are_visible(self.locators.ALL_SELECT_COLUMNS)
        list_select_column = []
        for item in all_select_columns:
            list_select_column.append(item)

        for item in range(len(list_select_column)):
            self.go_to_element(list_select_column[item])
            time.sleep(1)
            list_select_column[item].click()
            time.sleep(1)
            self.element_is_visible(self.locators.INPUT_SELECT_STATUS).send_keys(Keys.ARROW_DOWN)
            self.element_is_visible(self.locators.INPUT_SELECT_STATUS).send_keys(Keys.ENTER)
            time.sleep(1)

    # Заполнение остальных полей
    def change_editable_field_influencers(self):
        all_edite_columns_influencers_table = self.elements_are_visible(self.locators.ALL_EDITEVALUE_COLUMNS)

        date_list = []
        avg_views_list = []
        exp_er_list = []
        price_list = []
        remarks = []
        client_remarks = []

        for item in all_edite_columns_influencers_table:
            var = item.text
            if var == "Set date":
                date_list.append(item)
            elif var == "Set average views":
                avg_views_list.append(item)
            elif var == "Set Expected ER":
                exp_er_list.append(item)
            elif var == "Set price":
                price_list.append(item)
            elif var == "Add comments":
                remarks.append(item)
            elif var == "Add a client comment":
                client_remarks.append(item)

        for i in range(len(date_list)):
            self.go_to_element(date_list[i])
            time.sleep(1)
            date_list[i].click()
            self.element_is_visible(self.locators.INFLUENCERS_TUB).click()

        for i in range(len(avg_views_list)):
            self.go_to_element(avg_views_list[i])
            time.sleep(1)
            avg_views_list[i].click()
            self.element_is_visible(self.locators.AVG_VIEW).send_keys("111")
            self.element_is_visible(self.locators.INFLUENCERS_TUB).click()

        for i in range(len(exp_er_list)):
            self.go_to_element(exp_er_list[i])
            time.sleep(1)
            exp_er_list[i].click()
            self.element_is_visible(self.locators.EXP_ER).send_keys("80")
            self.element_is_visible(self.locators.INFLUENCERS_TUB).click()

        for i in range(len(price_list)):
            self.go_to_element(price_list[i])
            time.sleep(1)
            price_list[i].click()
            self.element_is_visible(self.locators.PRICE).send_keys("1500")
            self.element_is_visible(self.locators.INFLUENCERS_TUB).click()

        for i in range(len(remarks)):
            self.go_to_element(remarks[i])
            time.sleep(1)
            remarks[i].click()
            self.element_is_visible(self.locators.REMARKS).send_keys("Auto test Remarks")
            self.element_is_visible(self.locators.INFLUENCERS_TUB).click()

        for i in range(len(client_remarks)):
            self.go_to_element(client_remarks[i])
            time.sleep(1)
            client_remarks[i].click()
            self.element_is_visible(self.locators.REMARKS).send_keys("Auto test Client Remarks")
            self.element_is_visible(self.locators.INFLUENCERS_TUB).click()

    def change_editable_field_content(self):
        all_edite_columns_content_table = self.elements_are_visible(self.locators.ALL_EDITEVALUE_COLUMNS)
        other_editable_value_content_table = self.elements_are_visible(self.locators.OTHER_EDITABLE_VALUE_CONTENT_TABLE)

        spent_list = []
        views_list = []
        reach_list = []
        shares_list = []
        saves_list = []
        interactions_list = []
        clicks_list = []
        installs_list = []
        registrations_list = []
        depsits_list = []
        actions_list = []
        revenue_test = []
        remarks_list = []
        client_remarks_list = []

        for item in all_edite_columns_content_table:
            var = item.text
            if var == "Set total spent":
                spent_list.append(item)
            elif var == "Set total clicks":
                clicks_list.append(item)
            elif var == "Set total installs":
                installs_list.append(item)
            elif var == "Set total registrations":
                registrations_list.append(item)
            elif var == "Set total deposits":
                depsits_list.append(item)
            elif var == "Set total actions":
                actions_list.append(item)
            elif var == "Set total revenue":
                revenue_test.append(item)
            elif var == "Add comments":
                remarks_list.append(item)
            elif var == "Add a client comment":
                client_remarks_list.append(item)

        for item in other_editable_value_content_table:
            var = item.text
            if var == "Set total views":
                views_list.append(item)
            elif var == "Set total reach":
                reach_list.append(item)
            elif var == "Set total shares":
                shares_list.append(item)
            elif var == "Set total saves":
                saves_list.append(item)
            elif var == "Set total interactions":
                interactions_list.append(item)

        for i in range(len(spent_list)):
            self.go_to_element(spent_list[i])
            time.sleep(1)
            spent_list[i].click()
            self.element_is_visible(self.locators.SPENT).send_keys("42.23")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(views_list)):
            self.go_to_element(views_list[i])
            time.sleep(1)
            views_list[i].click()
            self.element_is_visible(self.locators.VIEWS).send_keys("99325.43")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(reach_list)):
            self.go_to_element(reach_list[i])
            time.sleep(1)
            reach_list[i].click()
            self.element_is_visible(self.locators.REACH).send_keys("3575.42")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(shares_list)):
            self.go_to_element(shares_list[i])
            time.sleep(1)
            shares_list[i].click()
            self.element_is_visible(self.locators.SHARES).send_keys("1445.54")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(saves_list)):
            self.go_to_element(saves_list[i])
            time.sleep(1)
            saves_list[i].click()
            self.element_is_visible(self.locators.SAVES).send_keys("323.34")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(interactions_list)):
            self.go_to_element(interactions_list[i])
            time.sleep(1)
            interactions_list[i].click()
            self.element_is_visible(self.locators.INTER).send_keys("9399.45")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(clicks_list)):
            self.go_to_element(clicks_list[i])
            time.sleep(1)
            clicks_list[i].click()
            self.element_is_visible(self.locators.CLICKS).send_keys("765.43")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(installs_list)):
            self.go_to_element(installs_list[i])
            time.sleep(1)
            installs_list[i].click()
            self.element_is_visible(self.locators.INSTALL).send_keys("3422332")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(registrations_list)):
            self.go_to_element(registrations_list[i])
            time.sleep(1)
            registrations_list[i].click()
            self.element_is_visible(self.locators.REGISTRATION).send_keys("2000")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(depsits_list)):
            self.go_to_element(depsits_list[i])
            time.sleep(1)
            depsits_list[i].click()
            self.element_is_visible(self.locators.DEPOSITS).send_keys("434.3")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(actions_list)):
            self.go_to_element(actions_list[i])
            time.sleep(1)
            actions_list[i].click()
            self.element_is_visible(self.locators.ACTION).send_keys("532.23")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(revenue_test)):
            self.go_to_element(revenue_test[i])
            time.sleep(1)
            revenue_test[i].click()
            self.element_is_visible(self.locators.REVENUE).send_keys("111.23")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(remarks_list)):
            self.go_to_element(remarks_list[i])
            time.sleep(1)
            remarks_list[i].click()
            self.element_is_visible(self.locators.REMARKS).send_keys("Lorem ipsum dolor sit amet, consectetur Remark")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

        for i in range(len(client_remarks_list)):
            self.go_to_element(client_remarks_list[i])
            time.sleep(1)
            client_remarks_list[i].click()
            self.element_is_visible(self.locators.REMARKS).send_keys(
                "Lorem ipsum dolor sit amet, consectetur Client Remark")
            self.element_is_visible(self.locators.CONTENT_TUB).click()

    def check_field_content_table(self):

        all_edite_columns_content_table_after = self.elements_are_present(self.locators.ALL_EDITEVALUE_COLUMNS_AFTER)
        other_editable_value_content_table_after = self.elements_are_present(
            self.locators.OTHER_EDITABLE_VALUE_CONTENT_TABLE_AFTER)

        list_for_check = []

        for item in all_edite_columns_content_table_after:
            var = item.text
            list_for_check.append(var)

        for item in other_editable_value_content_table_after:
            var = item.text
            list_for_check.append(var)

        return list_for_check

    def check_field_influencers_table(self):
        all_edite_columns = self.elements_are_visible(self.locators.CHECK_ALL_EDITEVALUE_COLUMNS)
        list_for_check = []
        for item in all_edite_columns:
            var = item.text
            list_for_check.append(var)
        return list_for_check

    def check_select_influencers_table(self):
        all_select_columns = self.elements_are_visible(self.locators.ALL_SELECT_COLUMNS)
        list_for_check_select = []
        for item in all_select_columns:
            var = item.text
            list_for_check_select.append(var)
        return list_for_check_select
