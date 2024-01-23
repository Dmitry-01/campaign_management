from selenium.webdriver.common.by import By


class ToolTipLocators:
    #check_tool_tips_header_table
    TOOL_TIPS = (By.CSS_SELECTOR, "div[role='tooltip'] span")
    INFLUENCER = (By.CSS_SELECTOR, "div[id='shape-title-channels'] div svg")
    CONTENT = (By.CSS_SELECTOR, "div[id='shape-title-content'] div svg")
    VIEWS = (By.CSS_SELECTOR, "div[id='shape-title-views'] div svg")
    CPM = (By.CSS_SELECTOR, "div[id='shape-title-cpm'] div svg")
    BUDGET = (By.CSS_SELECTOR, "div[id='shape-title-budget'] div svg")

    # check_tool_tips_influencer_table
    TOOL_TIPS_COLUMN_INFLUENCER_AND_CONTENT_TABLE = (By.CSS_SELECTOR, "div[role='tooltip'] span")
    INFLUECER_TABLE_STATUS_COLUMN = (By.CSS_SELECTOR, "th[id='status'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
    INFLUECER_TABLE_FORMAT = (By.CSS_SELECTOR, "th[id='format'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
    INFLUECER_TABLE_CATEGORY = (By.CSS_SELECTOR, "th[id='category'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
    INFLUECER_TABLE_CPM = (By.CSS_SELECTOR, "th[id='computedCPM'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
    INFLUECER_TABLE_ER = (By.CSS_SELECTOR, "th[id='er'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
    INFLUECER_TABLE_PRICE = (By.CSS_SELECTOR, "th[id='budget'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
    INFLUECER_TABLE_MANAGER = (By.CSS_SELECTOR, "th[id='manager'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")

    # go_to_the_content_table
    CONTENT_TAB = (By.CSS_SELECTOR, "div[class='css-16xd4id ehzqydi1']")

    # check_tool_tips_content_table
    CONTENT_TABLE_SPENT = (By.CSS_SELECTOR, "th[id='adSpent'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
    CONTENT_TABLE_ACTIONS = (By.CSS_SELECTOR, "th[id='adActions'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
    CONTENT_TABLE_CPM = (By.CSS_SELECTOR, "th[id='cpm'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
    CONTENT_TABLE_CPA = (By.CSS_SELECTOR, "th[id='cpa'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
    CONTENT_TABLE_CPD = (By.CSS_SELECTOR, "th[id='cpd'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
    CONTENT_TABLE_CPR = (By.CSS_SELECTOR, "th[id='cpr'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
    CONTENT_TABLE_CPI = (By.CSS_SELECTOR, "th[id='cpi'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
    CONTENT_TABLE_CPC = (By.CSS_SELECTOR, "th[id='cpc'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
    CONTENT_TABLE_CTR = (By.CSS_SELECTOR, "th[id='ctr'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
    CONTENT_TABLE_CR = (By.CSS_SELECTOR, "th[id='cr'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
    CONTENT_TABLE_ER = (By.CSS_SELECTOR, "th[id='er'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")