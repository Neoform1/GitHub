from .pages.main_page import MainPage
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):

    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    time.sleep(2)
    page.go_to_login_page()      # выполняем метод страницы — переходим на страницу логина
    time.sleep(2)

def test_guest_should_see_login_link(browser):

    page = MainPage(browser, link)
    page.open()
    time.sleep(2)
    page.should_be_login_link()
    time.sleep(2)

def test_quest_can_go_to_login_page(browser):
    
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()
    time.sleep(2)
