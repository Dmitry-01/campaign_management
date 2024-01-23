from selenium.webdriver.common.by import By


class TestInviteUsersLocators:
    # Тест-кейс test_invite_for_client()
    BUTTON_SHARE = (By.CSS_SELECTOR, "a[class='css-6ids85']")
    INPUT_EMAIL = (By.CSS_SELECTOR, "input[placeholder='Enter email to invite']")
    BUTTON_SEND_INVITE = (By.CSS_SELECTOR, "button[class='css-13dbxdy']")
    HREF_FIRST_CAMPAIGN = (By.CSS_SELECTOR, "a[class='css-cm8iok ejbzu8n38']")

    SIMPLE_LINK = (By.CSS_SELECTOR, "div a[class='css-cm8iok ejbzu8n38']")

    # Форма регистрации клиента
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    INPUT_FIRST_NAME = (By.CSS_SELECTOR, "input[name='firstName']")
    INPUT_LAST_NAME = (By.CSS_SELECTOR, "input[name='lastName']")
    I_AGREE_BUTTON = (By.CSS_SELECTOR, "span[class='ant-checkbox']")
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    # Инвайт в компанию
    INVITE_CAMPAIGN_NAME = (By.CSS_SELECTOR, "h1[class='css-b6gnge erzk1m57']")

    #Удаление из компании
    DELETE_BUTTON =(By.CSS_SELECTOR, "button[class='DeleteCell_button__BYuFG css-aqacxr'] span g")

    EMAIL = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    SIGNIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    DELETE_BUTTON_IN_MODAL = (By.CSS_SELECTOR, "button[class='css-1gjz7r']")

    CLIENT_EMAIL = (By.CSS_SELECTOR, "p[class='TeamUserCell_subtitle__ngwiR']")
    CAMPAIGN_LINK = (By.CSS_SELECTOR, 'div[class="css-16xd4id ehzqydi1"] a')
    #log_out
    DROPDOWN = (By.CSS_SELECTOR,"div[class='css-1tru4dg e1qgg9yb1']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR,'div[class="css-1wvtqye eomziv50"] svg path[d="M14 6v15H3v-2h2V3h9v1h5v15h2v2h-4V6h-3zm-4 5v2h2v-2h-2z"]')
    ALL_DROPDOWN_BUTTONS = (By.CSS_SELECTOR, 'a[class="css-1qaokd8-Block-Block eg7giwt2"]')
    #get_the_stub_text
    FIRST_TEXT = (By.CSS_SELECTOR, 'p[class="css-nixyqn ex7hddf3"]')
    SECONDE_TEXT = (By.CSS_SELECTOR, 'p[class="css-1bl4w8v ex7hddf4"]')