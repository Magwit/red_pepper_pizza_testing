from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# TODO Use save_screenshot and name the png file appropriatelyusing error message and
# possibly timestamp tooo for uniqueness. Only assertions warrant screenshots
# TODO audit xpaths w Locator Adviser: https://davertmik.github.io/locator/
# TODO consider if and how assert should be in functions -> extrapolate


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
    visible_order_footer_xpath = "//div[@class='order-footer']//input[@type!='hidden']"
    visible_order_footer = browser.find_elements(By.XPATH, visible_order_footer_xpath)
    print(len(visible_order_footer))

    # order-header div is empty | still empty
    # order-items div is empty | order-items div contains div/input
    # order-footer div has two hidden sum elements | order-footer has two input elements

    try:
        assert len(orders) == 0 and len(visible_order_footer) == 0
    except Exception as e:
        browser.save_screenshot("assert_order-deleted.png")
        print(type(e))
        raise e

    time.sleep(1)
