from .base_page import BasePage 
from selenium.common.exceptions import UnexpectedAlertPresentException
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
import time


class Page_Object(BasePage):

    def add_to_basket(self):
        
        add_to_basket_button = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET)
        assert self.is_element_present(*MainPageLocators.ADD_TO_BASKET), "no button add_to_cart"
        add_to_basket_button.click()
        # time.sleep(2)



    def name_and_price(self):

        name_of_book = self.browser.find_element(*MainPageLocators.NAME)
        assert self.is_element_present(*MainPageLocators.NAME), "no name of a book"
        print(f"Your name of a book: {name_of_book.text}")
        
        price_of_a_book = self.browser.find_element(*MainPageLocators.PRICE)
        assert self.is_element_present(*MainPageLocators.PRICE), "no price of a book"
        print(f"Your price of a book: {price_of_a_book.text}")

    # def go_to_basket(self):

    #     go_to_basket = self.browser.find_element(*MainPageLocators.GO_TO_Basket)
    #     assert self.is_element_present(*MainPageLocators.GO_TO_Basket), "no basket found"
    #     go_to_basket.click()
    #     time.sleep(2)


 



    