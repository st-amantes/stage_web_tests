import os
from selene import browser, have
from helpers.autorization_number_and_mail import autorization_maill

def test_collection_add(autorization_maill):
    browser.element('[data-qa="select-creation-item"]').click()
    browser.element('#navbar > div.navbar__navigation > div.selection-wrapper > div > div:nth-child(5)').click()
    browser.element('[data-qa="creation-title-area"]').send_keys('Первый ***')
    browser.element('[data-qa="creation-description-area"]').send_keys('Пост первый')



    browser.element('[data-qa="default-image-loader"]').send_keys \
        (os.path.abspath('../resources/avatar.jpg'))
    browser.element('[class="uploaded-photos__crop-button"]').click()
    browser.all('[class="nav-block__change"]').element_by(have.exact_text('Сохранить')).click()


    browser.all('[data-qa="creation-next-step-btn"]').element_by(have.exact_text('Создать')).click()
    browser.element('[class="c-black save-to-icon profile-icon"]').click()