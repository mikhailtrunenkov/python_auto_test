from .base_page import BasePage
from .locators import ProductPageLocators

class NegativePage(BasePage):
    def open_product_page(self):
       self.browser.get(self.url)
        
    def add_to_cart(self):
        # Вызов метода для проверки корректного url
        self.should_be_valid_url()
        
        # Нажимаем "Добавить в корзину"
        product_link = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        product_link.click()
        
         # Вызов метода с математической операцией из класса BasePage
        self.solve_quiz_and_get_code()
        
    def should_be_valid_url(self):
        # Проверяем, что '?promo=newYear' содержится в нашей ссылке
        assert 'promo=offer' in self.browser.current_url, 'url is not correct'

        # Проверяем отсутствие элемента с сообщением, что товар добавлен к корзину
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"
       
    def success_message_is_absent(self):
        assert self.is_disappeared(*ProductPageLocators.BASKET_VALUE), \
       "Element is showing, but should disappeard"
        