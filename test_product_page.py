from .pages.product_page import ProductPage
import pytest

# @pytest.mark.parametrize('number', [*range(7), pytest.param("7", marks=pytest.mark.xfail), *range(8,10)])
# def test_guest_can_add_product_to_basket(browser, number):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
#     page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#     page.open_product_page()           # открываем страницу
#     page.add_to_cart()                 # Добавляем товар
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

    