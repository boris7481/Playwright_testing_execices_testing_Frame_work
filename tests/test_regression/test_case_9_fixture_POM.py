# Test Case 9: Search Product
# •	1. Launch browser
# •	2. Navigate to url 'http://automationexercise.com'
# •	3. Verify that home page is visible successfully
# •	4. Click on 'Products' button
# •	5. Verify user is navigated to ALL PRODUCTS page successfully
# •	6. Enter product name in search input and click search button
# •	7. Verify 'SEARCHED PRODUCTS' is visible
# •	8. Verify all the products related to search are visible  je ne suis pas sur que cette condition est verifie par mon code


from playwright.sync_api import Page, expect, Playwright

import time

from pages.home_page import HomePage
from pages.products_page import ProductsPage


# Test Case 9: Search Product
# ---#termes = ID ,   .terms = class
# Test Case 6: Contact Us Form
def test_Search_Product(page: Page):
    # home page
    homepage = HomePage(page)
    homepage.navigate_without_login()
    homepage.selectordernavigationlink()
    # product page
    product_search = ProductsPage(page)
    product_search.navigate_to_see_all_products_page_and_seach_product()


# firefox
def test_Search_Product_firefox(test_login_User_firefox_consent):
    page = test_login_User_firefox_consent
    page.get_by_role("link", name="products").click()
    expect(page.get_by_text("All Products")).to_be_visible()
    page.get_by_placeholder("Search Product").fill("short")
    page.locator("#submit_search").click()
    expect(page.get_by_text("SEARCHED PRODUCTS")).to_be_visible()
