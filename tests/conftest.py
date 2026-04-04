import pytest
from playwright.sync_api import Page, expect, Playwright


@pytest.fixture
def go_to_page_einwilligen(page: Page):
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="Einwilligen").click()
    return page


@pytest.fixture
def go_to_page_login(page: Page):
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="Einwilligen").click()
    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_text("Login to your account")).to_be_visible()
    return page


@pytest.fixture
def fake_credentials():
    return {
        "email_fake": "flase@gmail.com",
        "password_fake": "Freedom95_fake",
    }


@pytest.fixture
def credentials_name_email():
    return {
        "name": "09w0823@Freedom",
        "email": "freedomvision@gmail.com",
    }


@pytest.fixture
def credentials_valid():
    return {
        "email": "freedomvision@gmail.com",
        "password": "Freedom95",
    }


# ---------------------  firefox  ----------------------------------
@pytest.fixture
def test_login_User_firefox_consent(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="consent").click()
    return page


@pytest.fixture
def test_login_User_firefox_login(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="consent").click()
    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_text("Login to your account")).to_be_visible()
    return page
