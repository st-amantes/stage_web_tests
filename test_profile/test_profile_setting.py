from selene import browser
from helpers.autorization_number import autorization_number
def test_setting_profile(autorization_number):
    browser.element('[data-qa="user-menu-button"]').click()
    browser.element('[data-qa="user-profile-settings-button"]').click()
    browser.element('[class="editor__background-action"]').click()