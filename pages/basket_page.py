from .base_page import BasePage
from .locators import MainPageLocators





class BasketPage(BasePage):
    
    def is_basket_empty(self):

        is_element_present = self.is_element_present(*MainPageLocators.EMPTY_BASKET)
        assert is_element_present, "YOUR BASKET_IS_NOT_EMPTY"

    def is_basket_not_empty(self):

        is_element_not_present = self.is_not_element_present(*MainPageLocators.EMPTY_BASKET)
        assert is_element_not_present, "YOUR BASKET_IS_EMPTY"        # 'negative check'

    def basket_empty_text_present(self):

        is_present = self.is_element_present(*MainPageLocators.YOUR_BASKET_IS_EMPTY_TEXT)
        assert is_present, "'Empty' text is not present"

    def basket_empty_text_not_present(self):
        
        is_not_present = self.is_not_element_present(*MainPageLocators.YOUR_BASKET_IS_EMPTY_TEXT)
        assert is_not_present, "'Empty' text is present"         # 'negative check'
