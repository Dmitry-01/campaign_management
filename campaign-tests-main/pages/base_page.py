import pymongo
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

from data.data import db_name


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def element_is_visible(self, locator, timeout=20):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=20):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=20):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=20):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({ inline: 'center', block: 'center' });", element)

    def switch_to_window(self, page_number):
        self.driver.switch_to.window(self.driver.window_handles[page_number])

    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def action_drag_and_drop_to_element(self, what, where):
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()

class MongoStorage():
    def __init__(self):
        self.mongo_uri ="mongodb://worker1.buzz.guru:27000,worker1.buzz.guru:27001,worker1.buzz.guru:27002,worker1.buzz.guru:27003,worker1.buzz.guru:27004,worker1.buzz.guru:27005,worker1.buzz.guru:27006,worker1.buzz.guru:27007,worker2.buzz.guru:27000,worker2.buzz.guru:27001,worker2.buzz.guru:27002,worker2.buzz.guru:27003,worker2.buzz.guru:27004,worker2.buzz.guru:27005,worker2.buzz.guru:27006,worker2.buzz.guru:27007,worker6.buzz.guru:27000,worker6.buzz.guru:27001,worker6.buzz.guru:27002,worker6.buzz.guru:27003,worker6.buzz.guru:27004,worker6.buzz.guru:27005,worker6.buzz.guru:27006,worker6.buzz.guru:27007,worker7.buzz.guru:27000,worker7.buzz.guru:27001,worker7.buzz.guru:27002,worker7.buzz.guru:27003,worker7.buzz.guru:27004,worker7.buzz.guru:27005,worker7.buzz.guru:27006,worker7.buzz.guru:27007/buzzguru_master"
        self.db_name = db_name
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.db_name]

    def get_code(self, email):
        item = self.db["permit"].find_one({"info.email": email})
        return item["code"]

    def get_permitId(self, email):
        item = self.db["permit"].find_one({"info.email": email})
        return item["_id"]

    def get_campaign(self, email):
        item = self.db["permit"].find_one({"info.email": email, "type": "campaign.invite"})
        return item["info"]["campaignId"]


