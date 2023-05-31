import allure
from selene import browser

from base_page.page_register_mail import BasePageRegister


@allure.title("Тест на регистрацию через кнопку 'Войти'")
def test_registration_mail():
    basepage = BasePageRegister()
    browser.open('')
    basepage.button_in()
    basepage.button_reg()
    basepage.input_email()
    basepage.input_password()
    basepage.reset_password()
    basepage.send_sms()
    basepage.confirm_button()
