import pytest
from selene import browser

@pytest.fixture(scope="session", autouse=True)
def driver_setting():
    browser.driver.set_window_size(1920, 1800)
    browser.driver.set_window_position(-2, -2)
    browser.config.base_url = 'https://dev-web.pfm.team/'
    yield

    # browser.quit()