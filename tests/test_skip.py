"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser


def is_mobile(widgh):
    return widgh < 1200

@pytest.fixture(params=[(1080, 1900), (600, 900 ), (450, 450)])
def setup_browser(request):
    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]
    browser.config.driver_name = 'firefox'


def test_github_desktop(setup_browser):
    if is_mobile(browser.config.window_width):
        pytest.skip('Тест для мобильных устройств')
    browser.open('https://github.com/')
    browser.element('[href="/login"]').click()


def test_github_mobile(setup_browser):
    if not is_mobile(browser.config.window_width):
        pytest.skip('Тест для десктопа')
    browser.open('https://github.com/')
    browser.element('[class*="rounded my-1"]').click()
    browser.element('[href="/login"]').click()
