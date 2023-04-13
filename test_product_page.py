from selenium.webdriver.common.by import By
from .pages.product_page import Page_Object
from .pages.main_page import BasePage # !

import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_add_item__to_basket(browser):

    page = Page_Object(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    # time.sleep(2)
    page.add_to_cart()
    time.sleep(2)
    page.name_and_price()


