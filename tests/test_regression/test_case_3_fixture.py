# Test Case 3: Login User with incorrect email and password
from playwright.sync_api import expect


def test_login_User_with_incorrect_email_and_password(go_to_page_login, fake_credentials):
    page = go_to_page_login
    page.locator('[data-qa="login-email"]').fill(fake_credentials["email"])
    page.locator('[data-qa="login-password"]').fill(fake_credentials["password"])
    page.locator('[data-qa="login-button"]').click()
    expect(page.get_by_text("Your email or password is incorrect!")).to_be_visible()


# Firefox
def test_login_User_with_incorrect_email_and_password_firefox(test_login_User_firefox_login, fake_credentials):
    page = test_login_User_firefox_login
    page.locator('[data-qa="login-email"]').fill(fake_credentials["email"])
    page.locator('[data-qa="login-password"]').fill(fake_credentials["password"])
    page.locator('[data-qa="login-button"]').click()
    expect(page.get_by_text("Your email or password is incorrect!")).to_be_visible()

