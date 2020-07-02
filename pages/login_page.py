from base_page import BasePage
from selenium.webdriver.common.by import By
from locators import MainPageLocators
from locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        #assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        assert "login" in self.browser.driver.current_url, "БЕБЕ"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма логина не найдена"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации не найдена"