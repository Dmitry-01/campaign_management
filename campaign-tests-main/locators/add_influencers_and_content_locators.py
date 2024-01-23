from selenium.webdriver.common.by import By


class AddInfluencersAndContentLocators:
    # Рекламная компания
    FIRST_CAMPAIGN = (By.CSS_SELECTOR, "a[class='css-cm8iok ejbzu8n38']")
    ADD_INFLUENCER_BUTTON = (By.CSS_SELECTOR, "button[class='css-13dbxdy']")
    INPUT_ENTER_LINK = (By.CSS_SELECTOR, "input[name='add-influencer-input']")
    INPUT_SEARCH = (By.CSS_SELECTOR, "input[class='css-1qj8cpv e1y4u8pz2']")
    SEARCH_CHANNEL = (By.CSS_SELECTOR, "div p[class='UserCell_title__r8uSD']")
    CONTENT_TAB = (By.LINK_TEXT, "Content")

    # Вкладка Content
    ADD_CONTENT_BUTTON = (By.CSS_SELECTOR, "button[class='css-13dbxdy']")
    INPUT_LINK = (By.CSS_SELECTOR, "input[name='link']")
    INSTAGRAM_TAB = (By.CSS_SELECTOR, "button[id='add-content-tab-instagram']")
    CONTENT_ADD_BUTTON_MODAL = (By.CSS_SELECTOR, "button[type='submit']")
    # INSTAGRAM_TAB = (By.CSS_SELECTOR, "button[id='add-content-tab-instagram']")
    TIKTOK_TAB = (By.CSS_SELECTOR, "button[id='add-content-tab-tiktok']")
    VIDEO_SEARCH_CHANNEL = (By.CSS_SELECTOR, "div[class='ContentUserCell_title__FMAmy']")
    ALL_SOCIAL_MEDIA_BUTTONS = (By.CSS_SELECTOR, "a[class = 'UserCell_iconWrapper__VVS4_']")
    TIKTOK_CHANNEL_TITLE = (By.CSS_SELECTOR,"h1[data-e2e='user-title']")
    INSTAGRAM_CHANNEL_TITLE = (By.CSS_SELECTOR,"h2[class='x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli "
                                               "x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty "
                                               "x1943h6x x1i0vuye x1ms8i2q xo1l8bm x5n08af x10wh9bi x1wdrske x8viiok "
                                               "x18hxmgj']")
    YOUTUBE_CHANNEL_TITLE = (By.CSS_SELECTOR,"span yt-formatted-string[id='channel-handle']")