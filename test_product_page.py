from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('number', [*range(7), pytest.param("7", marks=pytest.mark.xfail), *range(8,10)])
def test_guest_can_add_product_to_basket(browser, number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open_product_page()           # открываем страницу
    page.add_to_cart()                 # Добавляем товар
    