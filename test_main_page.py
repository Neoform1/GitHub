from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from selenium.webdriver.common.by import By
import time
import pytest



link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage():


    def test_guest_can_go_to_login_page(self, browser):

        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.browser.implicitly_wait(2)
        page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
        page.browser.implicitly_wait(2)


    def test_guest_should_see_login_link(self, browser):

        page = MainPage(browser, link)
        page.open()
        page.browser.implicitly_wait(2)
        page.should_be_login_link()
        page.browser.implicitly_wait(2)


    def test_quest_can_go_to_login_page(self, browser):
        
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_page()
        page.browser.implicitly_wait(2)



# step 4.3.10

@pytest.mark.step10
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):

    link = "http://selenium1py.pythonanywhere.com/en-gb/"

    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()

    page.is_basket_empty()
    page.basket_empty_text_present()


