"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser


@pytest.fixture
def desktop_config():
    browser.config.driver_name = 'firefox'
    browser.config.window_width = 1900
    browser.config.window_height = 1080
    browser.config.base_url = 'https://github.com'

@pytest.fixture
def mobile_config():
    browser.config.driver_name = 'firefox'
    browser.config.window_width = 642
    browser.config.window_height = 1024
    browser.config.base_url = 'https://github.com'


def test_github_desktop(desktop_config):
    browser.open('/')
    browser.element('[href="/login"]').click()


def test_github_mobile(mobile_config):
    browser.open('/')
    browser.element('[class*="rounded my-1"]').click()
    browser.element('[href="/login"]').click()
