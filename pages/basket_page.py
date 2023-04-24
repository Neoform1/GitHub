from .base_page import BasePage
from .locators import MainPageLocators





class BasketPage(BasePage):
    
    def is_basket_empty(self):

        is_element_present = self.is_element_present(*MainPageLocators.EMPTY_BASKET)
        assert is_element_present, "YOUR BASKET_IS_not_EMPTY"

        # is_element_not_present = self.is_not_element_present(*MainPageLocators.EMPTY_BASKET)
        # assert is_element_not_present, "'negative check' YOUR BASKET_IS_EMPTY"        # 'negative check'

    def basket_empty_text_present(self):

        is_present = self.is_element_present(*MainPageLocators.YOUR_BASKET_IS_EMPTY)
        assert is_present, "'Empty' text is not present"

        # is_not_present = self.is_not_element_present(*MainPageLocators.YOUR_BASKET_IS_EMPTY)
        # assert is_not_present, "'negative check' -Empty- text is present"         # 'negative check'
