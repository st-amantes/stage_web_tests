import random

from selene import browser, have
from random import randint
class BasePageRegisterNumber:
    def button_in(self):
        browser.element(".usermenu__sign-in").click()

    def button_reg(self):
        browser.element('[class="form-submit-btn #43adeb main-view__btn signUp"]').click()

    def button_number(self):
        browser.element('[data-qa="switch-button--enter"]').click()
    def send_number(self):
        browser.element('[class="form-input"]').send_keys(''.join([str(random.randint(0, 11)) for _ in range(11)]))

    def send_sms(self):
        browser.element('[data-qa="sign-in-button"]').click()

    def password_input(self):
        browser.element('[data-qa="reset-password-phone-code-input"]').send_keys('6666')
    def button_in_click(self):
        browser.element('[data-qa="sign-in-button"]').click()
