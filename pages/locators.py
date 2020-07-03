from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

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
    BUTTON_ADD = ('btn-add-to-basket')

class ProductPageLocators(object):
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")