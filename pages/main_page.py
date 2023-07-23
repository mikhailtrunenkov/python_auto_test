from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage): 
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
    
    def go_to_basket_page(self):
        link = self.browser.find_element(*MainPageLocators.BASKET_BTN)
        link.click()
        
    def product_should_not_be(self):
        self.should_be_valid_url()
        assert self.is_not_element_present(*MainPageLocators.PRODUCT_IN_BASKET), \
        "There is somthing in the basket, but should not be"
    
    def should_be_valid_url(self):
        assert 'basket/' in self.browser.current_url, 'url is not correct'
        
    def should_be_message_basket_empty(self):
        empty = self.browser.find_element(*MainPageLocators.EMPTY_BASKET)
        empty_basket = empty.text
        assert empty_basket == "Your basket is empty. Continue shopping", \
        "There is somthing in the basket"
        