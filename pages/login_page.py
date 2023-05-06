from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators

import time
import random


class LoginPage(BasePage):
    
    def should_be_login_page(self):

        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        
        login_url = self.browser.current_url
        assert login_url, "Login page url is not correct"

    def should_be_login_form(self):
        
        login_form = self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert login_form, "Login form is not displayed"

    def should_be_register_form(self):
        
        register_form = self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        assert register_form, "Register form is not displayed"

    def register_new_user(self):

        e_mail = str(time.time()) + "@fakemail.org"
        pw = (random.randrange(100000000000))


        email = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        assert email, "Email is not displayed"
        email.send_keys(e_mail)
    

        password = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        assert password, "Password is not displayed"
        password.send_keys(pw)

        password_2 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_2)
        assert password_2, "Password 2 is not displayed"
        password_2.send_keys(pw)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        assert register_button, "register button not found"
        register_button.click()
