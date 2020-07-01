from .pages.locators import *
from base_page import BasePage


class PageItems(BasePage):
    def can_add_product_to_basket(self):
        page = MainPage(browser, TOVAR_LINK)# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        add_to_button = self.browser.find_element(BUTTON_ADD)
        add_to_button.click()
        page.solve_quiz_and_get_code()