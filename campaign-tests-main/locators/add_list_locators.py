from selenium.webdriver.common.by import By


class AddListLocators:
    ADD_LIST_BUTTON = (By.CSS_SELECTOR, "button[class='css-obnuof']")
    CHOOSE_LIST = (By.CSS_SELECTOR, "div[class='css-2rgzri e1tcnqzv2']")
    ADD_LIST_MODAL_BUTTON = (By.CSS_SELECTOR, "div[class='css-o2q3zj'] button[class='css-13dbxdy']")
    TITLE_CHANNEL = (By.CSS_SELECTOR, "p[class='UserCell_title__r8uSD']")

    LIST = (By.CSS_SELECTOR, "a[id='lists']")
    LAST_LIST = (By.CSS_SELECTOR, "a[class='css-ww8wib-List-styles--HoverRowWrapper edzc4dq24']")
    TITLES_LIST = (By.CSS_SELECTOR, "div[class='css-1wgih93-title3 e1ptsmbf0']")

class AnalyticsListLocators:
    LIST = (By.CSS_SELECTOR, 'div[class="css-hsda3n eizaqzs0"] a[data-test="subbar-lists"]')
    YOUTUBE_LIST = (By.CSS_SELECTOR,'div[class="e11x9atp2 table-gird-row css-1b089rk-css-ItemRow"]')
    CREATE_CAMPAIGN_BUTTON = (By.CSS_SELECTOR, 'button[class="css-1cpmag6-Button-styles--Btn-Button-styles--Btn-Button-styles--Btn e1vgcyo62"] div[class="css-1e3tog6-Button-styles--Ripple e1vgcyo64"]')
    ALL_INFLUENCERS = (By.CSS_SELECTOR, 'div[class="css-1wgih93-title3 e1ptsmbf0"]')
    LIST_NAME = (By.CSS_SELECTOR, 'div[class="css-5mekwu el7dmc21"]')
    CAMPAIGN_NAME = (By.CSS_SELECTOR, 'h1[class="css-b6gnge erzk1m57"]')
    TITLES = (By.CSS_SELECTOR, 'p[class="UserCell_title__r8uSD"]')
