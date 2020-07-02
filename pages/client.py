import math

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException

from product_page import ProductPage


class Client():
    def __init__(self):
        self.browser = webdriver.Chrome()

    def load_page(self, url):
        self.browser.get(url)
        return ProductPage(self.browser)