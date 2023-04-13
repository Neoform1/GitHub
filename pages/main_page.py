from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import LoginPageLocators
import time

class MainPage(BasePage): 

    def go_to_login_page(self):

        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link not present"

    
    def should_be_login_link(self):   

        self.is_element_present(*MainPageLocators.LOGIN_LINK) 
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
    

    def should_be_login_page(self):

        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"

        