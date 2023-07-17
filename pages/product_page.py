from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
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
            
        # Сообщение о том, что товар добавлен в корзину. 
        # Название товара в сообщении долежн совпадать с тем товаром, который вы действительно добавили
        self.product_name_matches_the_one_added()
        
        # Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара
        self.equal_prices()
        
    def should_be_valid_url(self):
        # Проверяем, что '?promo=newYear' содержится в нашей ссылке
        assert 'promo=offer' in self.browser.current_url, 'url is not correct'

    def product_name_matches_the_one_added(self):
        # Проверяем наличие элемента с сообщением, что товар добавлен к корзину
        assert self.is_element_present(*ProductPageLocators.ALERT_INNER), 'Message about adding is not presented'
        # Находим элемент и переводим сообщение в текст
        message = self.browser.find_element(*ProductPageLocators.ALERT_INNER).text
        # Находим элемент и переводим название товара в текст
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        # Проверяем, что название товара в сообщении совпадает с товаром, который мы добавили 
        assert product_name == message, 'There is no such product in the message'

    def equal_prices(self):
        # Проверяем наличие элемента с сообщением о стоимости товара
        assert self.is_element_present(*ProductPageLocators.BASKET_VALUE), 'Cart value not shown'
        # Находим элемент с ценой в сообщении и переводим в текст
        basket_value = self.browser.find_element(*ProductPageLocators.BASKET_VALUE).text
        # Находим элемент с ценой товара и переводим в текст
        cost_of_good = self.browser.find_element(*ProductPageLocators.COST_OF_GOOD).text
        # Проверяем, что цена товара совпадает с ценой в сообщении
        assert cost_of_good == basket_value, 'The price of the cart does not match the price of the product'
        