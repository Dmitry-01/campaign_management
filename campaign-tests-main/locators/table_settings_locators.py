from selenium.webdriver.common.by import By


class CustomColumnLocators:
    SETTINGS_TABLE_BUTTON = (By.CSS_SELECTOR, "button[id='setting-table-button']")
    ADD_COLUMN = (By.CSS_SELECTOR,"button[class='css-1kmpuih']")
    TITLE_NAME = (By.CSS_SELECTOR,"input[name='title']" )
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "div button[type='submit']")
    COLUMN_TITLES = (By.CSS_SELECTOR, "th[class='ka-thead-cell ka-thead-cell-height ka-thead-fixed ka-thead-background ka-pointer static-cell']")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "div[class='css-1kruwhs ee1c2f16'] button[class='css-13dbxdy']")

class ResetToDefaultLocators:
    SETTINGS_TABLE_BUTTON = (By.CSS_SELECTOR, "button[id='setting-table-button']")
    COLUMNS = (By.CSS_SELECTOR, "span[class='HeadCellContent_title__26P_x']")
    RESET_TO_DEFAULTS_BUTTON = (By.CSS_SELECTOR, "button[class='css-vas5py']")
    X_BUTTON = (By.CSS_SELECTOR, "button[class='css-smi18i']")

class SwapTheColumnLocators:
    COLUMN = (By.CSS_SELECTOR, 'th[class="ka-thead-cell ka-thead-cell-height ka-thead-fixed ka-thead-background ka-pointer static-cell"]')
    STATUS_COLUMN = (By.CSS_SELECTOR, 'thead[class="ka-thead"] th[id="status"]')
    FORMAT_COLUMN = (By.CSS_SELECTOR, 'thead[class="ka-thead"] th[id="format"]')
