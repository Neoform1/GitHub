from selenium.webdriver.common.by import By
from .pages.product_page import Page_Object
import pytest
import time


# step 4.3.2

def test_guest_can_add_product_to_basket(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    page = Page_Object(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу

    page.add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)

# -----------










