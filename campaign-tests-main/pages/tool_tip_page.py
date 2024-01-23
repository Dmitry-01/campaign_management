import time

from locators.tool_tip_locators import ToolTipLocators
from pages.base_page import BasePage


class ToolTipPage(BasePage):
    locators = ToolTipLocators()

    def get_data_tooltip(self, hover_elem, all_tool_tips_locator):
        element = self.element_is_present(hover_elem)
        self.go_to_element(element)
        time.sleep(1)
        self.action_move_to_element(element)
        time.sleep(1)
        tool_tip_text = self.element_is_visible(all_tool_tips_locator)
        text = tool_tip_text.text
        return text

    def check_tool_tips_header_table(self):
        tool_tip_influencer = self.get_data_tooltip(self.locators.INFLUENCER, self.locators.TOOL_TIPS)
        tool_tip_content = self.get_data_tooltip(self.locators.CONTENT, self.locators.TOOL_TIPS)
        tool_tip_views = self.get_data_tooltip(self.locators.VIEWS, self.locators.TOOL_TIPS)
        tool_tip_cpm = self.get_data_tooltip(self.locators.CPM, self.locators.TOOL_TIPS)
        tool_tip_budget = self.get_data_tooltip(self.locators.BUDGET, self.locators.TOOL_TIPS)
        return tool_tip_influencer, tool_tip_content, tool_tip_views, tool_tip_cpm, tool_tip_budget

    def check_tool_tips_influencer_table(self):
        tool_tip_status = self.get_data_tooltip(self.locators.INFLUECER_TABLE_STATUS_COLUMN, self.locators.TOOL_TIPS_COLUMN_INFLUENCER_AND_CONTENT_TABLE)
        tool_tip_format = self.get_data_tooltip(self.locators.INFLUECER_TABLE_FORMAT, self.locators.TOOL_TIPS_COLUMN_INFLUENCER_AND_CONTENT_TABLE)
        tool_tip_category = self.get_data_tooltip(self.locators.INFLUECER_TABLE_CATEGORY, self.locators.TOOL_TIPS_COLUMN_INFLUENCER_AND_CONTENT_TABLE)
        tool_tip_cpm = self.get_data_tooltip(self.locators.INFLUECER_TABLE_CPM, self.locators.TOOL_TIPS_COLUMN_INFLUENCER_AND_CONTENT_TABLE)
        tool_tip_er = self.get_data_tooltip(self.locators.INFLUECER_TABLE_ER, self.locators.TOOL_TIPS_COLUMN_INFLUENCER_AND_CONTENT_TABLE)
        tool_tip_budget = self.get_data_tooltip(self.locators.INFLUECER_TABLE_PRICE, self.locators.TOOL_TIPS_COLUMN_INFLUENCER_AND_CONTENT_TABLE)
        tool_tip_manager = self.get_data_tooltip(self.locators.INFLUECER_TABLE_MANAGER, self.locators.TOOL_TIPS_COLUMN_INFLUENCER_AND_CONTENT_TABLE)
        return tool_tip_status, tool_tip_format, tool_tip_category, tool_tip_cpm, tool_tip_er, tool_tip_budget ,tool_tip_manager

    def go_to_the_content_table(self):
        self.element_is_visible(self.locators.CONTENT_TAB).click()

    def check_tool_tips_content_table(self):
        tool_tip_spent = self.get_data_tooltip(self.locators.CONTENT_TABLE_SPENT, self.locators.TOOL_TIPS_COLUMN_INFLUENCER_AND_CONTENT_TABLE)
        tool_tip_actions = self.get_data_tooltip(self.locators.CONTENT_TABLE_ACTIONS, self.locators.TOOL_TIPS_COLUMN_INFLUENCER_AND_CONTENT_TABLE)
        tool_tip_cpm = self.get_data_tooltip(self.locators.CONTENT_TABLE_CPM, self.locators.TOOL_TIPS_COLUMN_INFLUENCER_AND_CONTENT_TABLE)
        tool_tip_cpa = self.get_data_tooltip(self.locators.CONTENT_TABLE_CPA, self.locators.TOOL_TIPS_COLUMN_INFLUENCER_AND_CONTENT_TABLE)
        tool_tip_cpd = self.get_data_tooltip(self.locators.CONTENT_TABLE_CPD, self.locators.TOOL_TIPS_COLUMN_INFLUENCER_AND_CONTENT_TABLE)
        tool_tip_cpr = self.get_data_tooltip(self.locators.CONTENT_TABLE_CPR, self.locators.TOOL_TIPS_COLUMN_INFLUENCER_AND_CONTENT_TABLE)
        tool_tip_cpi = self.get_data_tooltip(self.locators.CONTENT_TABLE_CPI, self.locators.TOOL_TIPS_COLUMN_INFLUENCER_AND_CONTENT_TABLE)
        tool_tip_cpc = self.get_data_tooltip(self.locators.CONTENT_TABLE_CPI, self.locators.TOOL_TIPS_COLUMN_INFLUENCER_AND_CONTENT_TABLE)
        tool_tip_ctr = self.get_data_tooltip(self.locators.CONTENT_TABLE_CTR, self.locators.TOOL_TIPS_COLUMN_INFLUENCER_AND_CONTENT_TABLE)
        tool_tip_cr = self.get_data_tooltip(self.locators.CONTENT_TABLE_CR, self.locators.TOOL_TIPS_COLUMN_INFLUENCER_AND_CONTENT_TABLE)
        tool_tip_er = self.get_data_tooltip(self.locators.CONTENT_TABLE_ER, self.locators.TOOL_TIPS_COLUMN_INFLUENCER_AND_CONTENT_TABLE)
        return tool_tip_spent, tool_tip_actions, tool_tip_cpm, tool_tip_cpa, tool_tip_cpd, tool_tip_cpr, tool_tip_cpi, tool_tip_cpc, tool_tip_ctr, tool_tip_cr, tool_tip_er
