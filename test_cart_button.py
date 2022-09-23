
from selenium.webdriver.common.by import By


def test_finds_add_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(5)
    button = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form button.btn")
    assert len(button) > 0, "basket button not found"
