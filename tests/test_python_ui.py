import re
from playwright.sync_api import expect


def test_open_google():
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.google.com")

        assert "Google" in page.title()

        browser.close()


def test_google_search():
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.google.com")

        page.fill("input[name='q']", "Playwright Python")
        page.keyboard.press("Enter")

        page.wait_for_selector("text=Playwright")  # waits for results
        assert "Playwright" in page.content()

        browser.close()


def test_button_click():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")
        
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        page.wait_for_url("**/inventory.html")
        assert "inventory" in page.url

        browser.close()


def test_dropdown():
    from playwright.sync_api import sync_playwright
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/dropdown")
        
        page.select_option("#dropdown", "1")
        selected = page.locator("#dropdown").input_value()

        assert selected == "1"

        browser.close()


def test_assert_text():
    from playwright.sync_api import sync_playwright
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")

        page.click("button")           # start loading
        page.wait_for_selector("#finish")

        assert page.inner_text("#finish") == "Hello World!"

        browser.close()


def test_screenshot():
    from playwright.sync_api import sync_playwright
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://example.com")

        try:
            assert page.title() == "Not The Title"
        except AssertionError:
            page.screenshot(path="error.png")
            raise

        browser.close()