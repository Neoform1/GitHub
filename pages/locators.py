from selenium.webdriver.common.by import By


class MainPageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")

class LoginPageLocators():
    
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

