import allure
from selene import browser

from base_page.page_register_number import BasePageRegisterNumber


@allure.title("Тест на регистрацию через кнопку 'Войти' по номеру")
def test_registration_number():
    basepage = BasePageRegisterNumber()
    browser.open('')
    basepage.button_in()
    basepage.button_reg()
    basepage.button_number()
    basepage.send_number()
    basepage.send_sms()
    basepage.password_input()
    basepage.button_in_click()