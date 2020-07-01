from base_page import BasePage
from pages.locators import MainPageLocators



def test_guest_can_add_product_to_basket():
    page = BasePage(browser, TOVAR_LINK)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.can_add_product_to_basket() #Добавили в корзину и вычислили значение