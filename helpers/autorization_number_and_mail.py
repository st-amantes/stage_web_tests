import pytest
from selene import browser

from base_page.page_register_mail import BasePageRegister
from base_page.page_register_number import BasePageRegisterNumber



@pytest.fixture()
def autorization_number():
    basepage = BasePageRegisterNumber()
    browser.open('')
    basepage.button_in()
    basepage.button_reg()
    basepage.button_number()
    basepage.send_number()
    basepage.send_sms()
    basepage.password_input()
    basepage.button_in_click()


@pytest.fixture()
def registration_mail():
    bas = BasePageRegister()
    browser.open('')
    bas.button_in()
    bas.button_reg()
    bas.input_email()
    bas.input_password()
    bas.reset_password()
    bas.send_sms()
    bas.confirm_button()
