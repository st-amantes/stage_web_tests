import os
from selene import browser, have
from helpers.autorization_number_and_mail import registration_mail
import pytest

def test_setting_profile(registration_mail):
    browser.element('[data-qa="user-menu-button"]').click()
    browser.element('[data-qa="user-profile-settings-button"]').click()
    browser.element('[accept=".jpg, .jpeg, .png"].editor__input-img.background').send_keys\
        (os.path.abspath('../resources/avatar.jpg'))
    browser.all('[data-v-64bf7729].nav-block__change').element_by(have.exact_text('Сохранить')).click()


