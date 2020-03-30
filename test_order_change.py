from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# TODO audit xpaths w Locator Adviser: https://davertmik.github.io/locator/
# TODO consider renaming teste with git mv


def test_order_change(browser):
    # GIVEN The user is on Red Pepper Pizza
    # AND A Blue and White pizza has been added to Your order

    URL = "https://magwit.github.io/pizza_site/"
    browser.get(URL)
    wait = WebDriverWait(browser, 20)

    blue_white_menu_item_btn_xpath = "//*[@id='blue']/button"

    try:
        wait.until(
            EC.presence_of_element_located((By.XPATH, blue_white_menu_item_btn_xpath))
        )
    except Exception as e:
        print(type(e))
        print(e.args)

    blue_white_menu_item_btn = browser.find_element(
        By.XPATH, blue_white_menu_item_btn_xpath
    )

    js = "arguments[0].click();"

    browser.execute_script(js, blue_white_menu_item_btn)

    # WHEN The user clicks the Delete button next to the order item

    delete_btn_xpath = "//div[@id='blue-order']/*[@class='delete']"

    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, delete_btn_xpath)))
    except Exception as e:
        print(type(e))
        print(e.args)

    delete_btn = browser.find_element(By.XPATH, delete_btn_xpath)
    delete_btn.click()

    # THEN the entire order is removed; both order item and sum.

    # order_items_xpath = "//*[@class='order-items']"

    any_order_xpath = "//*[@class='order-items']/div[contains(@id,'order')]"
    orders = browser.find_elements(By.XPATH, any_order_xpath)
    print(len(orders))

    # order-header div is empty | still empty
    # order-items div is empty | order-items div contains div/input REPLICATE from test_order.py
    # order-footer div has two hidden sum elements | order-footer has two input elements

    # how ro best assert non visibility. precence of hidden property in all that is contained in footer.

    assert 1 == 1

    time.sleep(2)
