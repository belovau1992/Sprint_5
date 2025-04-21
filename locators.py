from selenium.webdriver.common.by import By

class Locators:
    #Локаторы для регистрации
    PERSONAL_ACCOUNT_BUTTON = [By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va']"]#Кнопка личный кабинет на главной странице
    REG_BUTTON = (By.CLASS_NAME, "Auth_link__1fOlj")# Ссылка чтобы зарегистрироваться
    NAME = (By.XPATH, "//div[label[contains(text(),'Имя')]]//input")#Поле Имя
    EMAIL = (By.XPATH, "//div[label[contains(text(),'Email')]]//input")#Поле email
    PASSWORD = (By.XPATH,"//div[@type='password']")#Поле пароля
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]") #Кнопка Зарегистрироваться

    LOGIN_BUTTON_IN_REG = (By.XPATH, "//a[contains(text(), 'Войти')]")#Кнопка войти в форме регистрации
    LOGIN_BUTTON_IN_PASSWORD = (By.XPATH, "//a[contains(text(), 'Войти')]")#Кнопка войти в форме восстановления пароля

    #Локаторы для авторизации
    LOGIN_BUTTON = (By.XPATH,"//button[contains(text(), 'Войти')]") #Кнопка войти на главной странице
    LOGIN_BUTTON_IN = (By.XPATH, "//button[contains(text(), 'Войти')]") #Кнопка войти на странице авторизации

    HEADER_TITLE = (By.CLASS_NAME,"AppHeader_header__nav__g5hnF") #Заголовок страницы
    FORGOT_PASSWORD_LINK=(By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")#ссылка "Восстановить пароль"
    LOGO_STELLAR_BURGERS_IN_LK = (By.XPATH, "//html/body/div/div/header/nav/div/a/svg") #Логотип Stellar Burgers в Личном кабинете
    EXIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")#Кнопка выход в личном кабинете

    #Локаторы Конструктора
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")  # Кнопка конструктор в личном кабинете
    BREAD_SECTION = (By.XPATH, "//span[contains(text(),'Булки')]")#Блок булки
    SAUCES_SECTION = (By.XPATH, "//span[contains(text(),'Соусы')]")#Блок соусы
    FILLINGS_SECTION = (By.XPATH, "//span[contains(text(),'Начинки')]")#Блок начинки

