from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Sprint_5.locators import Locators


class TestConstructor():
    def test_sauces_section(self,driver):
        sauces_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(*Locators.SAUCES_SECTION)
        )
        sauces_tab.click()
        active_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                *Locators.SAUCES_SECTION)
        )
        assert active_tab.is_displayed()

    def test_bread_section(self,driver):
        bread_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(*Locators.BREAD_SECTION)
        )
        bread_tab.click()
        active_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                *Locators.BREAD_SECTION)
        )
        assert active_tab.is_displayed()

    def test_fillings_section(self,driver):
        fillings_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(*Locators.FILLINGS_SECTION)
        )
        fillings_tab.click()
        active_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                *Locators.FILLINGS_SECTION)
        )
        assert active_tab.is_displayed()