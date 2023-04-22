from selenium.webdriver.common.by import By
from .pages.product_page import Page_Object
import pytest
import time


# step 4.3.2 and 4.3.3

def test_guest_can_add_product_to_basket(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    page = Page_Object(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу

    page.add_to_basket()
    page.solve_quiz_and_get_code()
    # time.sleep(2)

    page.name_and_price()
    time.sleep(10)

# -----------










