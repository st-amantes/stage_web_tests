import os
import allure
from selene import browser, have, command
from helpers.autorization_number_and_mail import autorization_maill

@allure.title('Редактирование ')
def test_setting_profile(autorization_maill):
    browser.element('[data-qa="user-menu-button"]').click()
    browser.element('[data-qa="user-profile-settings-button"]').click()

    browser.element('[accept=".jpg, .jpeg, .png"].editor__input-img.background').send_keys\
        (os.path.abspath('../resources/avatar.jpg'))
    browser.all('[data-v-64bf7729].nav-block__change').element_by(have.exact_text('Сохранить')).click()

    browser.element('[class="editor__input-img avatar"]').send_keys\
        (os.path.abspath('../resources/avatar.jpg'))
    browser.all('[data-v-64bf7729].nav-block__change').element_by(have.exact_text('Сохранить')).click()

    browser.element('[data-qa="login-input"]').set_value('atares')
    browser.element('[data-qa="name-input"]').set_value('Viktor')
    browser.element('[data-qa="city-input"]').set_value('Chikago')
    browser.element('[class="textarea__editor"]').set_value('aaaaaaaaaaaa, aaaa,a aaa a,aaaaa')


    browser.element('[data-qa="change-button"]').perform(command.js.scroll_into_view)
    browser.element('[data-qa="change-button"]').click()
