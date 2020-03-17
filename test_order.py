import pytest


def test_placing_order(browser):
    # Given The user is on Red pepper Pizza
    URL = "https://magwit.github.io/pizza_site/"
    browser.get(URL)

    # When The user clicks on the Add to order button below "Opera"
    # And The user clicks on the Add to otrder button below "Frutti di Mare"

    # Then Opera and Frutti di Mare appears as order items in Your order
    # And the sum of the order is the correct amount 13.50

    pass
