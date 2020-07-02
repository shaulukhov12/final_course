from selenium.webdriver.common.by import By

from base_page import BasePage
from locators import AddBasket


class ProductPage(BasePage):

    # секция аттрибутов
    @property
    def add_to_basket_button(self):
        btn = self.browser.find_element_by_class_name(AddBasket.BUTTON_ADD)
        return btn

    # секция методов
    def add_to_basket(self):
        self.add_to_basket_button.click()