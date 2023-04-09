import re
from playwright.sync_api import Page, expect


def test_homepage_has_BMI_CALCULATOR_TITLE_AND_CLICKING_BUTTON_STAYS_ON_PAGE(page: Page):
    page.goto("http://127.0.0.1:8000/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("BMI CALCULATOR"))

    # create a locator
    Calculate_BMI = page.locator("text=Calculate BMI")

    # Expect an attribute "to be strictly equal" to the value.

    # Click the get started link.
    Calculate_BMI.click()

    # Expects the URL to contain intro.
    expect(page).to_have_title(re.compile("BMI CALCULATOR"))