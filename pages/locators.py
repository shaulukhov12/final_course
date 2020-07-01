from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    TOVAR_LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class LoginPageLocators():
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASS = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASS_CONF = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.NAME, '[name="registration_submit"]')
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASS = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_BUTTON = (By.NAME, '[name = "login_submit"]')
    LOGIN_FORM = (By.ID, '#login_form')
    REGISTER_FORM = (By.ID, '#register_form')

class AddBasket():
    BUTTON_ADD = (By.CSS_SELECTOR, '.btn - add - to - basket')