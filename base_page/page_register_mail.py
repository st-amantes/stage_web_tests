from selene import browser, have


class BasePageRegister:
    def button_in(self):
        browser.element(".usermenu__sign-in").click()

    def button_reg(self):
        browser.element('[class="form-submit-btn #43adeb main-view__btn signUp"]').click()

    def button_in_in(self):
        browser.element('[class="form-submit-btn outlined #8ECEF3 main-view__btn signIn"]').click()

    def input_email(self):
        browser.element('[data-qa="reset-password-email-input"]').send_keys('evitviter@gmail.com')

    def input_password(self):
        browser.element('[data-qa="auth-password-input"]').send_keys('12341234')

    def reset_password(self):
        browser.element('[data-qa="reset-password-confirm-password-input"]').send_keys('12341234')

    def send_sms(self):
        browser.element('[data-qa="sign-in-button"]').click()

    def confirm_sms(self):
        browser.element('[data-qa="reset-password-phone-code-input"]').send_keys("7777")

    def confirm_button(self):
        browser.element('[data-qa="sign-in-button"]').click()
