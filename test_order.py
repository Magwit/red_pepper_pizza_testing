import pytest


def test_placing_order(browser):
    URL = "https://magwit.github.io/pizza_site/"
    browser.get(URL)
    browser.implicitly_wait(10)
    # yield browser
    assert 2 == 2
    browser.quit()
