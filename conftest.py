import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from curl import *
from data import Credentials
from locators import Locators
from faker import Faker

@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    driver = webdriver.Chrome(options=options)
    driver.get(main_site)
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.REGISTER_BUTTON).click()

    return driver

@pytest.fixture(scope="module")
def fake_data():
    return Faker("ru_RU")