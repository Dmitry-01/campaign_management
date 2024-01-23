from selenium.webdriver.common.by import By


class CampaignManagerLocators:
    EMAIL = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    CAMPAIGN_MANAGER = (By.CSS_SELECTOR, "a[id='campaigns']")
    DEMO_CAMPAIGN = (By.CSS_SELECTOR, "div h1[class='css-b6gnge erzk1m57']")
    CLICK_DEMO_CAMPAIGN = (By.CSS_SELECTOR, "img[alt='Demo Campaign']")
    HEADER_TEXT = (By.CSS_SELECTOR, "div[class='e1rjmpf80 css-515t3v e6d6d743']")

    # FOLDER LOCATORS
    ADD_FOLDER_BUTTON = (By.CSS_SELECTOR, "button[id = 'create-folder-button']")
    FOLDER_NAME = (By.CSS_SELECTOR, "input[id='title']")
    FOLDER_DESCRIPTION = (By.CSS_SELECTOR, "div textarea[name='description']")
    NEXT_BUTTON = (By.CSS_SELECTOR, "div button[type='submit']")
    CREATE_FOLDER_BUTTON = (By.CSS_SELECTOR, "div button[type='submit']")
    TEXT_FOLDER_NAME = (By.CSS_SELECTOR, "div h1[class='css-b6gnge erzk1m57']")
    TEXT_FOLDER_DESCRIPTION = (By.CSS_SELECTOR, "div span[class='css-4xf3h7 e1tpsucn2']")

    # TEST_FOLDER = (By.CSS_SELECTOR, "div img[alt='New Folder Test Folder Automation']")
    TEST_FOLDER = (By.CSS_SELECTOR, "a button[class='ejknwvb0 css-17bzlf']")
    BUTTON_SETTINGS = (By.CSS_SELECTOR, "div button[class='css-1ekcgu4']")
    FOLDER_SETTINGS = (By.CSS_SELECTOR, "div a[id='popover-folder-settings']")
    DELETE_FOLDER = (By.CSS_SELECTOR, "div button[id='popover-folder-remove']")

    SAVE_BUTTON = (By.CSS_SELECTOR, "div button[class='css-13dbxdy']")

    ITEM_LIST = (By.CSS_SELECTOR, "div a[class='css-a3wc37 e13lhbob15']")

    FIRTS_TEST_FOLDER = (By.CSS_SELECTOR, "a[href^='/campaigns/folder'] div div div img")

    # Проверка отображения модалки при нажатии на кнопку удалить папку(страница список папкок)
    FOLDER_BUTTON_SETTINGS = (By.CSS_SELECTOR, "div button[class='egyjzwi3 css-17bzlf']")
    FOLDER_BUTTON_DELETED = (By.CSS_SELECTOR, "button[class='css-k5l913 egyjzwi2']")
    POPUP_DELETE_FOLDER = (By.CSS_SELECTOR, "div[class='css-1tdihow e4dpcyt1']")

    # ЛОКАТОРЫ ДЛЯ РЕКЛАМНОЙ КОМПАНИИ

    CREATE_CAMPAIGN_BUTTON = (By.CSS_SELECTOR, "div button[id='create-campaign-button']")
    INPUT_CAMPAIGN_NAME = (By.CSS_SELECTOR, "div input[name='title']")
    # Страница Campaign
    INPUT_CAMPAIGN_DATES = (By.CSS_SELECTOR, "div input[class='css-iymk2s e1mlhrtt1']")
    All_VALUE_DATE = (By.CSS_SELECTOR,
                      'button.react-calendar__tile.react-calendar__month-view__days__day:not(.react-calendar__month-view__days__day--neighboringMonth)')
    INPUT_PLANNED_BUDGET = (By.CSS_SELECTOR, "div input[name='budget']")
    INPUT_TOTAL_VIEWS = (By.CSS_SELECTOR, "div input[name='totalViews']")
    INPUT_EXPECTED_CPM = (By.CSS_SELECTOR, "div input[name='expectedCPM']")
    INPUT_EXPECTED_CPC = (By.CSS_SELECTOR, "div input[name='expectedCPC']")
    INPUT_CAMPAIGN_DESCRIPTION = (By.CSS_SELECTOR, "div input[name='expectedCPC']")
    BUTTON_NEXT = (By.CSS_SELECTOR, "div button[type='submit']")

    # Странца Requirements
    SELECT_GEO = (By.CSS_SELECTOR, "div.css-1cekyng.e1griy0w0")
    CHECK_BOX_ALL_COUNTRY = (By.CSS_SELECTOR, "button.css-1bpcdc2.eztje8e6")
    CLICK_GEO_AGAIN = (By.CSS_SELECTOR, "div.css-q9lhrr.e1griy0w0")

    AGES = (By.CSS_SELECTOR, "div[id='react-select-select-age-placeholder']")
    ALL_AGES_CHECK_BOX = (By.CSS_SELECTOR, ".react-select__menu.css-1nmdiq5-menu")

    PLATFORMS = (By.CSS_SELECTOR, "div[id='react-select-select-platform-placeholder']")
    ALL_PLATFORMS = (By.CSS_SELECTOR, "div[id='react-select-select-platform-listbox']")
    CLOSE_PLATFORMS_DROPDOWN = (By.CSS_SELECTOR,
                                "div [class = 'react-select__control react-select__control--is-focused react-select__control--menu-is-open css-t3ipsp-control']")


    CATEGORY = (By.CSS_SELECTOR, "div[id='react-select-select-category-placeholder']")
    ALL_CATEGORY = (By.CSS_SELECTOR, "div[id='react-select-select-category-listbox']")
    CLOSE_CATGORY_DROPDOWN = (By.CSS_SELECTOR,
                              "div[class = 'react-select__control react-select__control--is-focused react-select__control--menu-is-open css-t3ipsp-control']")

    # Странца Team
    CREATE_CAMPAIGN_BUTTON_TEAM_PAGE = (By.CSS_SELECTOR, "button[type='submit']")

    CAMPAIGN_NAME_INSIDE_CAMPAIGN_TEXT = (By.CSS_SELECTOR, "div h1[class='css-b6gnge erzk1m57']")
    CAMPAIGN_NAME_SPISOK_KOMPANII_TEXT = (By.CSS_SELECTOR, "span[id='overflow-tooltip']")
    FIRST_CAMPAIGN = (By.CSS_SELECTOR, "a[class='css-fxzijg esp0itm0']")

    ALL_CAMPAIGNS_SETTINGS_BUTTON = (By.CSS_SELECTOR, 'a[class="css-fxzijg esp0itm0"] button svg')
    DELETE_CAMPAIGN_BUTTON = (By.CSS_SELECTOR,"button[class='css-1gjz7r']" )
# class AddInfluencersAndContentLocators:
#     # Рекламная компания
#     FIRST_CAMPAIGN = (By.CSS_SELECTOR, "a[class='css-cm8iok ejbzu8n38']")
#     ADD_INFLUENCER_BUTTON = (By.CSS_SELECTOR, "button[class='css-13dbxdy']")
#     INPUT_ENTER_LINK = (By.CSS_SELECTOR, "input[name='add-influencer-input']")
#     INPUT_SEARCH = (By.CSS_SELECTOR, "input[class='css-1qj8cpv e1y4u8pz2']")
#
#     SEARCH_CHANNEL = (By.CSS_SELECTOR, "div p[class='UserCell_title__r8uSD']")
#
#     CONTENT_TAB = (By.LINK_TEXT, "Content")
#
#     # Вкладка Content
#     # Видео
#
#     ADD_CONTENT_BUTTON = (By.CSS_SELECTOR, "button[class='css-13dbxdy']")
#     INPUT_LINK = (By.CSS_SELECTOR, "input[name='link']")
#     INSTAGRAM_TAB = (By.CSS_SELECTOR, "button[id='add-content-tab-instagram']")
#
#     CONTENT_ADD_BUTTON_MODAL = (By.CSS_SELECTOR, "button[type='submit']")
#     INSTAGRAM_TAB = (By.CSS_SELECTOR, "button[id='add-content-tab-instagram']")
#     TIKTOK_TAB = (By.CSS_SELECTOR, "button[id='add-content-tab-tiktok']")
#     VIDEO_SEARCH_CHANNEL = (By.CSS_SELECTOR, "div[class='ContentUserCell_title__FMAmy']")
#     ALL_SOCIAL_MEDIA_BUTTONS = (By.CSS_SELECTOR, "a[class = 'UserCell_iconWrapper__VVS4_']")
#     TIKTOK_CHANNEL_TITLE = (By.CSS_SELECTOR,"h1[data-e2e='user-title']")
#     INSTAGRAM_CHANNEL_TITLE = (By.CSS_SELECTOR,"h2[class='x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli "
#                                                "x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty "
#                                                "x1943h6x x1i0vuye x1ms8i2q xo1l8bm x5n08af x10wh9bi x1wdrske x8viiok "
#                                                "x18hxmgj']")
#     YOUTUBE_CHANNEL_TITLE = (By.CSS_SELECTOR,"span yt-formatted-string[id='channel-handle']")

# class TestInviteUsersLocators:
#     # Тест-кейс test_invite_for_client()
#     BUTTON_SHARE = (By.CSS_SELECTOR, "a[class='css-6ids85']")
#     INPUT_EMAIL = (By.CSS_SELECTOR, "input[placeholder='Enter email to invite']")
#     BUTTON_SEND_INVITE = (By.CSS_SELECTOR, "button[class='css-13dbxdy']")
#     HREF_FIRST_CAMPAIGN = (By.CSS_SELECTOR, "a[class='css-cm8iok ejbzu8n38']")
#
#     SIMPLE_LINK = (By.CSS_SELECTOR, "div a[class='css-cm8iok ejbzu8n38']")
#
#     # Форма регистрации клиента
#     INPUT_PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
#     INPUT_FIRST_NAME = (By.CSS_SELECTOR, "input[name='firstName']")
#     INPUT_LAST_NAME = (By.CSS_SELECTOR, "input[name='lastName']")
#     I_AGREE_BUTTON = (By.CSS_SELECTOR, "span[class='ant-checkbox']")
#     SIGN_UP_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
#
#     # Инвайт в компанию
#     INVITE_CAMPAIGN_NAME = (By.CSS_SELECTOR, "h1[class='css-b6gnge erzk1m57']")


class TableCampaignPageLocators:
    #Очистка всех полей
    # MAIN_CHECKBOX = (By.CSS_SELECTOR, "input#checkbox-cmdSelection")
    POINT_BUTTON = (By.CSS_SELECTOR, "td[class='ka-cell  sticky-cell-right sticky-cell-tbody']")

    TWO_BUTTONS = (By.CSS_SELECTOR,"button[class='css-ld2wqo egyjzwi2']")

    CLEAR_BUTTON = (By.CSS_SELECTOR, "button[class='css-1y2dtbm']")

    # Заполнение полей в таблице

    ALL_SELECT_COLUMNS = (By.CSS_SELECTOR, "div span[class='SelectableValue_title__NzLvp']")
    MANAGER = (By.CSS_SELECTOR, ".SelectableValue_title__UjyUF")
    INPUT_SELECT_STATUS = (By.CSS_SELECTOR, "input[class='react-select__input']")
    ROW_CATEGORY = (By.CSS_SELECTOR, "th[id='category']")
    ROW_MANAGER = (By.CSS_SELECTOR, "th[id='manager']")
    ROW_CLIENT_DECISION = (By.CSS_SELECTOR, "th[id='clientDecision']")
    ROW_REMARKS = (By.CSS_SELECTOR, "th[id='clientNotes']")
    ALL_ROWS = (By.CSS_SELECTOR,
                "th[class='ka-thead-cell ka-thead-cell-height ka-thead-fixed ka-thead-background ka-pointer  static-cell']")
    ROW_STATUS = (By.CSS_SELECTOR, "th[id='status']")
    ROW_DATE_ADDED = (By.CSS_SELECTOR, "th[id='addedAt']")

    TABLE = (By.CSS_SELECTOR, "div[class='ka-table-wrapper']")

    ALL_EDITEVALUE_COLUMNS = (By.CSS_SELECTOR, "div[class='EditableValue_value__SLdZn EditableValue_editable__nHdRG EditableValue_empty__sODgF']")
    OTHER_EDITABLE_VALUE_CONTENT_TABLE = (By.CSS_SELECTOR,"div[class='StyledValue_value__bz5OG StyledValue_empty___i6eP StyledValue_editable___eCjP']")

    CHECK_ALL_EDITEVALUE_COLUMNS = (By.CSS_SELECTOR, "div[class='EditableValue_value__SLdZn EditableValue_editable__nHdRG']")
    INFLUENCERS_TUB = (By.CSS_SELECTOR, "div[class='css-16xd4id ehzqydi1']")
    CONTENT_TUB = (By.CSS_SELECTOR, "div[class='css-16xd4id ehzqydi1']")
    #TAB INFLUENCERS
    AVG_VIEW = (By.CSS_SELECTOR, "input[name='avg']")
    EXP_ER = (By.CSS_SELECTOR, "input[name='er']")
    PRICE = (By.CSS_SELECTOR, "input[name='budget']")
    REMARKS = (By.CSS_SELECTOR, "textarea[class='css-6092ww e1kpri800']")

    DATE_TEXT = (By.CSS_SELECTOR, "div[class='EditableValue_value__VGU4i EditableValue_editable__01_T']")
    #TAB CONTENT
    SPENT = (By.CSS_SELECTOR, "input[name='adSpent']")
    VIEWS = (By.CSS_SELECTOR, "input[name='views']")
    REACH = (By.CSS_SELECTOR, "input[name='uniqViewers']")
    SHARES = (By.CSS_SELECTOR, "input[name='shares']")
    SAVES = (By.CSS_SELECTOR, "input[name='saves']")
    INTER = (By.CSS_SELECTOR, "input[name='interactions']")
    CLICKS = (By.CSS_SELECTOR, "input[name='adClicks']")
    INSTALL = (By.CSS_SELECTOR, "input[name='adInstalls']")
    REGISTRATION = (By.CSS_SELECTOR, "input[name='adRegistrations']")
    DEPOSITS = (By.CSS_SELECTOR, "input[name='adDeposits']")
    ACTION = (By.CSS_SELECTOR, "input[name='adActions']")
    REVENUE = (By.CSS_SELECTOR, "input[name='adRevenue']")

    ALL_EDITEVALUE_COLUMNS_AFTER = (By.CSS_SELECTOR, 'div[class="EditableValue_value__SLdZn EditableValue_editable__nHdRG"]')
    OTHER_EDITABLE_VALUE_CONTENT_TABLE_AFTER = (By.CSS_SELECTOR, 'div[class="StyledValue_value__bz5OG StyledValue_editable___eCjP"]')

# class DownloadTablePageLocators:
#     # BUTTONS_TABLE = (By.CSS_SELECTOR, "button[class='css-aqacxr']")
#     EXPORT_BUTTON = (By.CSS_SELECTOR, "button[id='export-modal-button']")
#     BUTTONS_TABLE_DOWMLOAD = (By.CSS_SELECTOR, "button[id='download-table-button']")
#     TITLE_CAMPAIGN = (By.CSS_SELECTOR, "h1[class='css-b6gnge erzk1m57']")


# class AddListLocators:
#     ADD_LIST_BUTTON = (By.CSS_SELECTOR, "button[class='css-obnuof']")
#     CHOOSE_LIST = (By.CSS_SELECTOR, "div[class='css-2rgzri e1tcnqzv2']")
#     ADD_LIST_MODAL_BUTTON = (By.CSS_SELECTOR, "div[class='css-o2q3zj'] button[class='css-13dbxdy']")
#     TITLE_CHANNEL = (By.CSS_SELECTOR, "p[class='UserCell_title__r8uSD']")

# class CustomColumnLocators:
#     SETTINGS_TABLE_BUTTON = (By.CSS_SELECTOR, "button[id='setting-table-button']")
#     ADD_COLUMN = (By.CSS_SELECTOR,"button[class='css-1kmpuih']")
#     TITLE_NAME = (By.CSS_SELECTOR,"input[name='title']" )
#     SUBMIT_BUTTON = (By.CSS_SELECTOR, "div button[type='submit']")
#     COLUMN_TITLES = (By.CSS_SELECTOR, "th[class='ka-thead-cell ka-thead-cell-height ka-thead-fixed ka-thead-background ka-pointer  static-cell']")
#     CLOSE_BUTTON = (By.CSS_SELECTOR, "div[class='css-1kruwhs ee1c2f16'] button[class='css-13dbxdy']")
#
# class ResetToDefaultLocators:
#     SETTINGS_TABLE_BUTTON = (By.CSS_SELECTOR, "button[id='setting-table-button']")
#     COLUMNS = (By.CSS_SELECTOR, "span[class='HeadCellContent_title__26P_x']")
#     RESET_TO_DEFAULTS_BUTTON = (By.CSS_SELECTOR, "button[class='css-vas5py']")
#     X_BUTTON = (By.CSS_SELECTOR, "button[class='css-smi18i']")

# class ToolTipLocators:
#     #check_tool_tips_header_table
#     TOOL_TIPS = (By.CSS_SELECTOR, "div[role='tooltip'] span")
#     INFLUENCER = (By.CSS_SELECTOR, "div[id='shape-title-channels'] div svg")
#     CONTENT = (By.CSS_SELECTOR, "div[id='shape-title-content'] div svg")
#     VIEWS = (By.CSS_SELECTOR, "div[id='shape-title-views'] div svg")
#     CPM = (By.CSS_SELECTOR, "div[id='shape-title-cpm'] div svg")
#     BUDGET = (By.CSS_SELECTOR, "div[id='shape-title-budget'] div svg")
#
#     # check_tool_tips_influencer_table
#     TOOL_TIPS_COLUMN_INFLUENCER_AND_CONTENT_TABLE = (By.CSS_SELECTOR, "div[role='tooltip'] span")
#     INFLUECER_TABLE_STATUS_COLUMN = (By.CSS_SELECTOR, "th[id='status'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
#     INFLUECER_TABLE_FORMAT = (By.CSS_SELECTOR, "th[id='format'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
#     INFLUECER_TABLE_CATEGORY = (By.CSS_SELECTOR, "th[id='category'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
#     INFLUECER_TABLE_CPM = (By.CSS_SELECTOR, "th[id='computedCPM'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
#     INFLUECER_TABLE_ER = (By.CSS_SELECTOR, "th[id='er'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
#     INFLUECER_TABLE_PRICE = (By.CSS_SELECTOR, "th[id='budget'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
#     INFLUECER_TABLE_MANAGER = (By.CSS_SELECTOR, "th[id='manager'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
#
#     # go_to_the_content_table
#     CONTENT_TAB = (By.CSS_SELECTOR, "div[class='css-16xd4id ehzqydi1']")
#
#     # check_tool_tips_content_table
#     CONTENT_TABLE_SPENT = (By.CSS_SELECTOR, "th[id='adSpent'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
#     CONTENT_TABLE_ACTIONS = (By.CSS_SELECTOR, "th[id='adActions'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
#     CONTENT_TABLE_CPM = (By.CSS_SELECTOR, "th[id='cpm'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
#     CONTENT_TABLE_CPA = (By.CSS_SELECTOR, "th[id='cpa'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
#     CONTENT_TABLE_CPD = (By.CSS_SELECTOR, "th[id='cpd'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
#     CONTENT_TABLE_CPR = (By.CSS_SELECTOR, "th[id='cpr'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
#     CONTENT_TABLE_CPI = (By.CSS_SELECTOR, "th[id='cpi'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
#     CONTENT_TABLE_CPC = (By.CSS_SELECTOR, "th[id='cpc'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
#     CONTENT_TABLE_CTR = (By.CSS_SELECTOR, "th[id='ctr'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
#     CONTENT_TABLE_CR = (By.CSS_SELECTOR, "th[id='cr'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")
#     CONTENT_TABLE_ER = (By.CSS_SELECTOR, "th[id='er'] span[class='HeadCellContent_actionWrapper__IIs__'] div svg")

