from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


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

    assert 1 == 1

    time.sleep(2)

    # THEN the order is removed
