from selenium.webdriver.common.by import By


class DownloadTablePageLocators:
    # BUTTONS_TABLE = (By.CSS_SELECTOR, "button[class='css-aqacxr']")
    EXPORT_BUTTON = (By.CSS_SELECTOR, "button[id='export-modal-button']")
    BUTTONS_TABLE_DOWMLOAD = (By.CSS_SELECTOR, "button[id='download-table-button']")
    TITLE_CAMPAIGN = (By.CSS_SELECTOR, "h1[class='css-b6gnge erzk1m57']")