from .base_page import BasePage 
from selenium.common.exceptions import UnexpectedAlertPresentException
from .locators import MainPageLocators
from .locators import ProductPageLocators

from selenium.webdriver.common.by import By
import time


class Page_Object(BasePage):

    def add_to_basket(self):
        
        add_to_basket_button = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET)
        assert self.is_element_present(*MainPageLocators.ADD_TO_BASKET), "no button add_to_cart"
        add_to_basket_button.click()



    def name_and_price(self):

        name_of_book = self.browser.find_element(*MainPageLocators.NAME)
        name_in_basket = self.browser.find_element(*MainPageLocators.NAME_IN_BASKET)
        assert name_of_book.text == name_in_basket.text
        print(f"Your name of a book: {name_of_book.text}")
        print(f"Your name of a book in basket: {name_in_basket.text}")
        
        price_of_a_book_in_basket = self.browser.find_element(*MainPageLocators.PRICE_IN_BASKET)
        print(f"Your price of a book in basket: {price_of_a_book_in_basket.text}")



    def should_not_be_success_message(self):

        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_be_success_message(self):
        
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Sucess message is not presented, but should be"

 



    