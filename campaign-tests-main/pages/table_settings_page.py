import time
from seletools.actions import drag_and_drop


from locators.table_settings_locators import CustomColumnLocators, ResetToDefaultLocators, SwapTheColumnLocators
from pages.base_page import BasePage


class CustomColumn(BasePage):
    locators = CustomColumnLocators()

    def add_custom_column(self):
        self.element_is_visible(self.locators.SETTINGS_TABLE_BUTTON).click()
        self.element_is_visible(self.locators.ADD_COLUMN).click()
        self.element_is_visible(self.locators.TITLE_NAME).send_keys("Custom field Text")
        time.sleep(1)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(self.locators.CLOSE_BUTTON).click()

    def check_add_custom_column(self):
        column_titles = self.elements_are_visible(self.locators.COLUMN_TITLES)
        column_titles_list = []
        for item in range(len(column_titles)):
            a = column_titles[item].text
            column_titles_list.append(a)
        return column_titles_list


class ResetToDefaultPage(BasePage):
    locators = ResetToDefaultLocators()

    def check_column_list_before(self):
        column_before = self.elements_are_present(self.locators.COLUMNS)
        column_list_before = []
        for item in column_before:
            i = item.text
            column_list_before.append(i)
        return column_list_before

    def click_on_the_reset(self):
        self.element_is_visible(self.locators.SETTINGS_TABLE_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(self.locators.RESET_TO_DEFAULTS_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(self.locators.X_BUTTON).click()
        time.sleep(1)

    def check_column_list_after(self):
        column_after = self.elements_are_present(self.locators.COLUMNS)
        column_list_after = []
        for item in column_after:
            i = item.text
            column_list_after.append(i)
        return column_list_after

class SwapTheColumnPage(BasePage):
    locators = SwapTheColumnLocators()

    def get_list_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_column(self):
        column_before = self.get_list_items(self.locators.COLUMN)
        drag_column = self.element_is_visible(self.locators.STATUS_COLUMN)
        drop_column = self.element_is_visible(self.locators.FORMAT_COLUMN)
        drag_and_drop(self.driver, drag_column, drop_column)
        column_after = self.get_list_items(self.locators.COLUMN)
        return column_before, column_after
