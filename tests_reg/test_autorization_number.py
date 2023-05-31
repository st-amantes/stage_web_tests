import allure_pytest.utils
import pytest
from selene import browser

from base_page.page_autorization_number import BasePageAutoNumber


@pytest.mark.skip('Пока что не реализован функционал сайта')
def test_autorization_number():
    basepage = BasePageAutoNumber()
    browser.open('')
    basepage.button_in()
    basepage.bitton_number()
    basepage.click_number()
    basepage.number()
    # basepage.enter_button()
    # basepage.password_number()
    # basepage.submit()
