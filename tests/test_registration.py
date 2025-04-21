from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Sprint_5.data import Credentials
from Sprint_5.helper import generate_registration_data
from Sprint_5.locators import Locators

from Sprint_5.curl import main_site


class TestRegistrationWithNewCredentials:

    def test_sucsess_registration(self, driver):
        #arrange
        name,email, password = generate_registration_data()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        #act
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.HEADER_TITLE))
        #assert
        assert driver.current_url == main_site + '/account/profile'

    def test_registration_invalid_password(self, driver):
        #arrange
        name,email = generate_registration_data()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys("1234")#Пароль меньше 6 символов
        #act
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.HEADER_TITLE))
        #assert
        assert driver.current_url != main_site + 'account/profile'

