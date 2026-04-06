import pytest
from playwright.sync_api import Page, expect, Playwright
import time
import json
from pages.home_page import HomePage
from pages.login_page import LoginPage
# just to check
# Test Case 4: Logout User
# ---#termes = ID ,   .terms = class
# Test Case : LVerify logout user

with open("data/credentials.json") as file:
    test_data_valid = json.load(file)
    print(test_data_valid)
    user_credentials_valid_list = test_data_valid["valid_user_credentials"]


# user_credentials_valid or parameter ist the variable and user_credentials_valid_list is the itarable
@pytest.mark.smoke
@pytest.mark.parametrize("user_credentials_valid", user_credentials_valid_list)
def test_Logout_User(page: Page, user_credentials_valid):
    user_name = user_credentials_valid["email"]
    password = user_credentials_valid["password"]

    logout_user = HomePage(page)
    logout_user.navigate_without_login()
    logout_user.selectordernavigationlink()

    loginPage = LoginPage(page)  # object for loginPage class
    loginPage.login(user_name, password)

    logout_user.logout_user_from_home_page()


# firefox
def test_Logout_User_firefox(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="consent").click()
    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_text("Login to your account")).to_be_visible()
    page.locator('[data-qa="login-email"]').fill("freedomvision@gmail.com")
    page.locator('[data-qa="login-password"]').fill("Freedom95")
    page.locator('[data-qa="login-button"]').click()
    expect(page.get_by_text("Logged in as 09w0823@Freedom")).to_be_visible()
    page.get_by_role("link", name="logout").click()
    expect(page.get_by_text("Login to your account")).to_be_visible()
    firefoxBrowser.close()

