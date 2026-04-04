from playwright.sync_api import expect


class CartPage:
    def __init__(self, page):
        self.page = page

    def check_the_product_in_cart(self):
        expect(self.page.get_by_text("Blue Top").first).to_be_visible()
        expect(self.page.get_by_text("Men Tshirt").first).to_be_visible()

