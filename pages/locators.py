from selenium.webdriver.common.by import By


class MainPageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button") 

    NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    
    VIEW_BASKET = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")

    EMPTY_BASKET = (By.CSS_SELECTOR, "#default > div.container-fluid.page > div") # blank basket 
    YOUR_BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")

class LoginPageLocators():
    
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
    
class ProductPageLocators():

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(2) > div")

class BasePageLocators():
    
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
