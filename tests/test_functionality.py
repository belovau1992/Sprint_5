from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Sprint_5.locators import Locators
from Sprint_5.curl import main_site


class TestFinctionality():

    def test_navigation_to_constructor_on_constructor_button(self,login): #Тест перехода по клику на "Конструктор" из личного кабинета
        login.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(login, 10).until(EC.visibility_of_element_located(Locators.HEADER_TITLE))
        assert login.current_url == main_site

    def test_logout(self,login,driver): # Тест выхода из аккаунта
        login.find_element(*Locators.EXIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.HEADER_TITLE))
        assert login.current_url == main_site
        assert driver.find_element(*Locators.LOGIN_BUTTON)