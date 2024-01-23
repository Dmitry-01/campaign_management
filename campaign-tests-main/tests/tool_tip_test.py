import time
import allure
import pytest

from pages.add_influencers_and_content_page import AddInfluencersAndContentPage
from pages.elements_page import CampaignManagementPage
from pages.tool_tip_page import ToolTipPage


@allure.feature("Test tool tip")
class TestToolTip:
    @pytest.mark.order(17)
    @allure.title("Checking tool tip in the campaign header")
    def test_tool_tip(self, driver):
        campaign_management_page = CampaignManagementPage(driver)
        tool_tip = ToolTipPage(driver)
        campaign_management_page.open_campaign()
        campaign_management_page.go_to_the_first_item_folder()
        campaign_management_page.go_to_the_first_campaign()
        time.sleep(1)
        tool_tip_influencer, tool_tip_content, tool_tip_views, tool_tip_cpm, tool_tip_budget = tool_tip.check_tool_tips_header_table()
        assert tool_tip_influencer == "Number of influencers and their prices by the 4 most used statuses", "hover missding or incorrect content"
        assert tool_tip_content == "Number of drafts and publications in the campaign", "hover missding or incorrect content"
        assert tool_tip_views == "Number of actual content views compared to the planned (set in the campaign settings)", "hover missding or incorrect content"
        assert tool_tip_cpm == "Value of the actual CPM compared to the planned one (set in the campaign settings)", "hover missding or incorrect content"
        assert tool_tip_budget == "Total budget - planned budget for the campaign (set in the settings). Closed budget - budget spent on published content", "hover missding or incorrect content"

    @pytest.mark.order(18)
    @allure.title("Checking tool tip in the column influencer table")
    def test_tool_tip_influencer_table(self, driver):
        campaign_management_page = CampaignManagementPage(driver)
        tool_tip = ToolTipPage(driver)
        campaign_management_page.open_campaign()
        campaign_management_page.go_to_the_first_item_folder()
        campaign_management_page.go_to_the_first_campaign()
        time.sleep(3)
        tool_tip_status, tool_tip_format, tool_tip_category, tool_tip_cpm, tool_tip_er, tool_tip_budget, tool_tip_manager = tool_tip.check_tool_tips_influencer_table()
        assert tool_tip_status == "Choose a phase of work with an influencer", "incorrect tooltip in status column column"
        assert tool_tip_format == "Choose an advertising format", "incorrect tooltip in format column"
        assert tool_tip_category == "Choose influencer category", "incorrect tooltip in category column"
        assert tool_tip_cpm == "Cost per thousand views. Based on AVG views and price", "incorrect tooltip in cpm column"
        assert tool_tip_er == "Estimated amount of interaction can earns relative to reach. Based on an assessment of the influencer's existing content", "incorrect tooltip in er column"
        assert tool_tip_budget == "Enter the estimated advertising budget for a particular influencer", "incorrect tooltip in budget column"
        assert tool_tip_manager == "Enter manager", "incorrect tooltip in manager column"

    @pytest.mark.order(19)
    @allure.title("Checking tool tip in the column content table")
    def test_tool_tip_content_table(self, driver):
        campaign_management_page = CampaignManagementPage(driver)
        tool_tip = ToolTipPage(driver)
        add_influencers_and_content_page = AddInfluencersAndContentPage(driver)
        campaign_management_page.open_campaign()
        campaign_management_page.go_to_the_first_item_folder()
        campaign_management_page.go_to_the_first_campaign()
        time.sleep(3)
        add_influencers_and_content_page.go_to_the_content_page()
        time.sleep(1)
        tool_tip_spent, tool_tip_actions, tool_tip_cpm, tool_tip_cpa, tool_tip_cpd, tool_tip_cpr, tool_tip_cpi, tool_tip_cpc, tool_tip_ctr, tool_tip_cr, tool_tip_er = tool_tip.check_tool_tips_content_table()
        time.sleep(1)
        assert tool_tip_spent == "Enter the budget spent on advertising per unit of content", f"incorrect {tool_tip_spent}"
        assert tool_tip_actions == "Enter the number of targeted actions achieved due to content that contains advertising. Example of target action - reaching level X in the game", f"incorrect {tool_tip_actions}"
        assert tool_tip_cpm == "Cost per thousand views for a particular content", f"incorrect {tool_tip_cpm}"
        assert tool_tip_cpa == "Cost per target action for a particular content", f"incorrect {tool_tip_cpa}"
        assert tool_tip_cpd == "Cost per deposit for a particular content", f"incorrect {tool_tip_cpd}"
        assert tool_tip_cpr == "Cost per registration for a particular content", f"incorrect {tool_tip_cpr}"
        assert tool_tip_cpi == "Cost per install for a particular content", f"incorrect {tool_tip_cpi}"
        assert tool_tip_cpc == "Cost per install for a particular content", f"incorrect {tool_tip_cpc}"
        assert tool_tip_ctr == "Click-through rate, shows what percentage of people click on the link after viewing the ad. Calculated as the ratio of clicks to views", f"incorrect {tool_tip_ctr}"
        assert tool_tip_cr == "Conversion rate, shows how many people have done the target action in relation to the total number of actions. Calculated as the number of targeted actions divided by the number of clicks. Target actions used to calculate in order to priority: deposits, actions, registrations, installs", f"incorrect {tool_tip_cr}"
        assert tool_tip_er == "Ratio of likes, comments and other interactions to content views", f"incorrect {tool_tip_er}"
