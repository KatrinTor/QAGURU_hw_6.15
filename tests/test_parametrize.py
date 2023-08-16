"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser


@pytest.fixture(
    scope='function',
    autouse=True,
    params=[(1250, 768), (1900, 1080), (375, 667), (400, 850)]
)
def browser_manager(request):
    browser.config.driver_name = 'firefox'
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield
    browser.quit()


@pytest.mark.parametrize('browser_manager', [(1250, 768), (1900, 1080)], indirect=True)
def test_github_desktop():
    browser.open('/')
    browser.element('[href="/login"]').click()


@pytest.mark.parametrize('browser_manager', [(375, 667), (400, 850)], indirect=True)
def test_github_mobile():
    browser.open('/')
    browser.element('[class*="rounded my-1"]').click()
    browser.element('[href="/login"]').click()