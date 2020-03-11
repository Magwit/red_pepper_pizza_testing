import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions


@pytest.fixture
def browser():
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    driver = Chrome(options=options)

    yield driver
    driver.quit()
