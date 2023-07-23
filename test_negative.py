from .pages.negative_page import NegativePage
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

@pytest.mark.xfail
def test_guest_can_add_product_to_basket(browser):
    page = NegativePage(browser, link)    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open_product_page()              # открываем страницу
    page.add_to_cart()                    # Добавляем товар
    page.should_not_be_success_message()  # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

def test_guest_cant_see_success_message(browser): 
    page = NegativePage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open_product_page()             # Открываем страницу товара 
    page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser): 
    page = NegativePage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open_product_page()           # открываем страницу
    page.add_to_cart()                 # Добавляем товар в корзину
    page.success_message_is_absent()   # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    