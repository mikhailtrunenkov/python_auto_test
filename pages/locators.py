from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BTN = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")
    EMPTY_BASKET = (By.ID, "content_inner")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "h2.col-sm-6")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_INNER = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    BASKET_VALUE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    COST_OF_GOOD = (By.CSS_SELECTOR, 'p.price_color')
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")