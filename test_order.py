import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_placing_order(browser):
    # Given The user is on Red pepper Pizza
    URL = "https://magwit.github.io/pizza_site/"
    browser.get(URL)

    opera_order_xpath = "//form[@id='oper']/button"
    frutti_order_xpath = "//form[@id='frut']/button"
    order_items_xpath = "//*[@class='order-items']"
    order_items = browser.find_element(By.XPATH, order_items_xpath)

    wait = WebDriverWait(browser, 20)

    try:
        # wait.until(
        #     EC.presence_of_all_elements_located((opera_order_btn, frutti_order_btn))
        # )
        wait.until(EC.element_to_be_clickable((By.XPATH, opera_order_xpath)))
    except Exception as e:
        print(e.args)

    # When The user clicks on the Add to order button below "Opera"
    opera_order_btn = browser.find_element(By.XPATH, opera_order_xpath)
    opera_order_btn.click()

    # And The user clicks on the Add to order button below "Frutti di Mare"

    frutti_order_btn = browser.find_element(By.XPATH, frutti_order_xpath)
    frutti_order_btn.click()

    # Then Opera and Frutti di Mare appears as order items in Your order

    # xpath for the two order divs for Opera and Frutti di Mare
    div_xpath = "//*[@class='order-items']/div[@id='oper-order' or @id='frut-order']"

    order_content = browser.find_elements_by_xpath(div_xpath)

    no_order_items = len(order_content)

    assert no_order_items == 2

    # And the sum of the order is the correct amount 13.50

    time.sleep(2)
    pass
