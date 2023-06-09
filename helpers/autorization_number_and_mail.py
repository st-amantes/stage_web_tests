import pytest
from selene import browser
from base_page.page_autorization import BasePageAuto
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
def autorization_maill():
    basepage = BasePageAuto()
    browser.open('')
    basepage.button_in()
    basepage.button_come()
    basepage.send_mail()
    basepage.send_password()
    basepage.enter_button()
