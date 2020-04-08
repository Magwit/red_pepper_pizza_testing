from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search_menu_item(browser):

    # GIVEN The user is on Red pepper Pizza

    URL = "https://magwit.github.io/pizza_site/"
    browser.get(URL)

    wait = WebDriverWait(browser, 20)

    # WHEN The user searches for olives

    try:
        search_bar = browser.find_element(By.ID, "pizza-search")
        search_bar.send_keys("olives")
    except Exception as e:
        print(type(e))
        print(e.args)

    # THEN the menu is filtered to display only Opera and Frutti di Mare

    # wait for elements to be hidden
    try:
        wait.until_not(
            EC.visibility_of_any_elements_located(
                (By.XPATH, "//formm[@class='itemform']")
            )
        )
    except Exception as e:
        print(type(e))
        print(e.arg)

    display_matches_xath = "//form[@class='itemForm'][@style!='display: none;']"
    ingredient_matches_xpath = "//form/p[contains(text(), 'olives')]"

    display_matches = browser.find_elements(By.XPATH, display_matches_xath)
    ingredient_matches = browser.find_elements(By.XPATH, ingredient_matches_xpath)

    try:
        assert len(display_matches) == len(ingredient_matches)
    except Exception as e:
        browser.save_screenshot("assert_search_results.png")
        print(e.args)
        raise e
