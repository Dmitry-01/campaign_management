import time

from data import data
from locators.invite_user_locators import TestInviteUsersLocators
from pages.base_page import BasePage, MongoStorage


class TestInviteUsersPage(BasePage):
    locators = TestInviteUsersLocators()

    def get_campaignid(self):
        return self.element_is_visible(self.locators.HREF_FIRST_CAMPAIGN).text

    def send_invite(self):
        self.element_is_visible(self.locators.BUTTON_SHARE).click()
        self.element_is_visible(self.locators.INPUT_EMAIL).send_keys(data.client_email)
        time.sleep(5)
        self.element_is_visible(self.locators.BUTTON_SEND_INVITE).click()
        print(data.client_email)

    def get_mongo_data(self):
        data_from_mongodb = MongoStorage()
        code = data_from_mongodb.get_code(data.client_email)
        permitid = data_from_mongodb.get_permitId(data.client_email)
        self.campaignId = data_from_mongodb.get_campaign(data.client_email)
        full_client_link = (
            f"https://staging.buzz.guru/auth/inviteCampaign?permitId={permitid}&code={code}&campaignId={self.campaignId}")
        return full_client_link

    def fill_form_client_registration(self):
        self.element_is_visible(self.locators.INPUT_PASSWORD).send_keys(data.client_email)
        self.element_is_visible(self.locators.INPUT_FIRST_NAME).send_keys("Dima")
        self.element_is_visible(self.locators.INPUT_LAST_NAME).send_keys("Test")
        self.element_is_visible(self.locators.I_AGREE_BUTTON).click()
        time.sleep(3)
        self.element_is_visible(self.locators.SIGN_UP_BUTTON).click()
        return data.client_email

    def check_invite_campaign_name(self):
        return self.element_is_visible(self.locators.INVITE_CAMPAIGN_NAME).text

    def get_client_email(self):
        self.element_is_visible(self.locators.BUTTON_SHARE).click()
        client_email = self.elements_are_visible(self.locators.CLIENT_EMAIL)
        client_email_list = []
        for item in client_email:
            email = item.text
            client_email_list.append(email)
        campaign = self.element_is_present(self.locators.CAMPAIGN_LINK)
        campaign_link = campaign.get_attribute('href')
        return client_email_list[1], campaign_link

    def delete_user_from_campaign(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()
        self.element_is_visible(self.locators.DELETE_BUTTON_IN_MODAL).click()

    def log_out(self):
        self.element_is_visible(self.locators.DROPDOWN).click()
        self.element_is_visible(self.locators.LOGOUT_BUTTON).click()

    def client_log_in(self, client_email):
        self.element_is_visible(self.locators.EMAIL).send_keys(f"{client_email}")
        self.element_is_visible(self.locators.PASSWORD).send_keys(f"{client_email}")
        self.element_is_visible(self.locators.SIGNIN_BUTTON).click()

    def go_to_the_campaign_link(self, campaign_link):
        campaign_page = f"{campaign_link}"
        self.open(campaign_page)

    def get_the_stub_text(self):
        stub_text_1 = self.element_is_visible(self.locators.FIRST_TEXT).text
        stub_text_2 = self.element_is_visible(self.locators.SECONDE_TEXT).text
        return stub_text_1, stub_text_2



