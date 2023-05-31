from selene import browser


class BasePageAutoNumber:
    def button_in(self):
        browser.element(".usermenu__sign-in").click()
    def bitton_number(self):
        browser.element('[class="form-submit-btn outlined #8ECEF3 main-view__btn signIn"]').click()
    def click_number(self):
        browser.element('[data-qa="switch-button--enter"]').click()

    def number(self):
        browser.element('[class="form-input"]').send_keys('12345678900')

    def enter_button(self):
        browser.element('[class="form-submit-btn #43adeb form-submit-btn"]').click()
    def password_number(self):
        browser.element('[data-qa="reset-password-phone-code-input"]').send_keys('6666')
    def submit(self):
        browser.element('class="form-submit-btn #43adeb form-submit-btn"').click()