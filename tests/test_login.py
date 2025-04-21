from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Sprint_5.locators import Locators
from Sprint_5.curl import main_site


class TestLogin():

    def test_login_from_page(self,driver): # Тест входа по кнопке «Войти в аккаунт» на главной странице
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert driver.current_url == main_site + '/login'

    def test_login_from_button_personal_account(self,driver): # Тест входа по кнопке «Личный кабинет» на главной странице
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.HEADER_TITLE))
        assert driver.current_url == main_site + '/login'

    def test_login_from_register_form(self,driver): # Тест входа по кнопке "Войти" в форме регистрации
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.LOGIN_BUTTON_IN_REG).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.HEADER_TITLE))
        assert driver.current_url == main_site + '/login'

    def test_login_from_forgot_password_form(self,driver): # Тест входа по кнопке "Войти" в форме восстановления пароля
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.FORGOT_PASSWORD_LINK).click()
        driver.find_element(*Locators.LOGIN_BUTTON_IN_PASSWORD).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.HEADER_TITLE))
        assert driver.current_url == main_site + '/login'
