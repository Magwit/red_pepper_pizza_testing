from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# TODO record gifs and then remove sleep
# TODO screenshots on error


def test_placing_order(browser):
    # GIVEN The user is on Red pepper Pizza
    URL = "https://magwit.github.io/pizza_site/"
    browser.get(URL)

    opera_order_xpath = "//form[@id='oper']/button"
    frutti_order_xpath = "//form[@id='frut']/button"

    wait = WebDriverWait(browser, 20)

    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, opera_order_xpath)))
    except Exception as e:
        print(type(e))
        print(e.args)

    # WHEN The user clicks on the Add to order button below "Opera"

    opera_order_btn = browser.find_element(By.XPATH, opera_order_xpath)
    opera_order_btn.click()

    # AND The user clicks on the Add to order button below "Frutti di Mare"

    frutti_order_btn = browser.find_element(By.XPATH, frutti_order_xpath)
    frutti_order_btn.click()

    # THEN Opera and Frutti di Mare appears as order items in Your order

    try:
        # wait.until(browser.find_elements(By.XPATH, "//*[@class='order-items']/*"))
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='order-items']/*"))
        )
    except Exception as e:
        print(type(e))
        print(e.args)

    # xpath for the two order divs for Opera and Frutti di Mare
    div_xpath = "//*[@class='order-items']/div[@id='oper-order' or @id='frut-order']"

    order_content = browser.find_elements(By.XPATH, div_xpath)

    # assert that the two specific order items are nested in the order-items div
    try:
        assert len(order_content) == 2
    except Exception as e:
        browser.save_screenshot("assert_order_items_created.png")
        print(e.args)
        raise e

    # AND the sum of the order is the correct amount 13.50

    sum_input_xpath = "//input[@name='total']"
    sum_input = browser.find_element(By.XPATH, sum_input_xpath).get_property("value")

    try:
        assert sum_input == "13.50"
    except Exception as e:
        browser.save_screenshot("assert_total_amount.png")
        print(e.args)
        raise e

    time.sleep(2)
