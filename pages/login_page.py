from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "login" in self.current_url

    def should_be_login_form(self):
        # проверка формы логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form didn't find"

    def should_be_register_form(self):
        # проверка формы регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form didn't find"