from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestConstructor():
    def test_sauces_section(self,driver):
        sauces_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Соусы')]"))
        )
        sauces_tab.click()
        active_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'tab_type_current') and contains(text(), 'Соусы')]"))
        )
        assert active_tab.is_displayed()

    def test_bread_section(self,driver):
        bread_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Булки')]"))
        )
        bread_tab.click()
        active_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'tab_type_current') and contains(text(), 'Булки')]"))
        )
        assert active_tab.is_displayed()

    def test_fillings_section(self,driver):
        fillings_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Начинки')]"))
        )
        fillings_tab.click()
        active_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'tab_type_current') and contains(text(), 'Начинки')]"))
        )
        assert active_tab.is_displayed()