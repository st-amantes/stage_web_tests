from selene import browser

from base_page.page_autorization import BasePageAuto


def test_autorization_mail():
    basepage = BasePageAuto()
    browser.open('')
    basepage.button_in()
    basepage.button_come()
    basepage.send_mail()
    basepage.send_password()
    basepage.enter_button()