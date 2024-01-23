import time
from telnetlib import EC

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService, Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC


# @pytest.fixture(scope="function")
# def driver():
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.maximize_window()
#     yield driver
#     driver.quit()



@pytest.fixture(scope="function")
def driver():
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    # chrome
    # driver = webdriver.Chrome(ChromeDriverManager(version='114.0.5735.90').install())
    # firefox
    # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    options = Options()
    options.add_argument('--headless')
    options.page_load_strategy = 'normal'
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    url = 'https://staging.buzz.guru/auth/login'
    driver.get(url)
    # try:
    #     element_0 = WebDriverWait(driver, 30).until(
    #         EC.presence_of_element_located((By.TAG_NAME, 'html'))
    #     )
    #     print("Тестируем root 1")
    #     print(element_0.get_attribute("outerHTML"))
    #     element = WebDriverWait(driver, 30).until(
    #         EC.presence_of_element_located((By.ID, 'notify'))
    #
    #     )
    #     print("Тестируем root 2")
    #     print(element.get_attribute("outerHTML"))
    # except TimeoutException as e:
    #     print(f"TimeoutException: {e}")
    #     driver.quit()
    time.sleep(5)
    login = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'email')))
    login.send_keys("d.serakov+testing@buzzguru.com")
    password = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'password')))
    password.send_keys("d.serakov+testing@buzzguru.com")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f'Screenshot {time}')
    driver.quit()

