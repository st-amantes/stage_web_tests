from selene import browser


class BasePageAuto:
    def button_in(self):
        browser.element('.usermenu__sign-in').click()

    def button_come(self):
        browser.element('[class="form-submit-btn outlined #8ECEF3 main-view__btn signIn"]').click()

    def send_mail(self):
        browser.element('[placeholder="Логин/e-mail"]').send_keys('evitviter@gmail.com')

    def send_password(self):
        browser.element('[data-qa="auth-password-input"]').send_keys('vitl121')

    def enter_button(self):
        browser.element('[data-qa="sign-in-button"]').click()
