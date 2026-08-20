import re
from pages.base_page import BasePage


class LotDetailsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.lot_title = self.page.locator("h1").first
        self.bid_section = self.page.get_by_test_id("lot-bid-status-section")
        self.bidding_counter = self.page.get_by_test_id("lot-bidding-counter")
        self.bid_status_bar = self.page.get_by_test_id("bid-status-bar")
        self.favourites_button = self.page.get_by_test_id("lot-card-favorite-button").first
        self.shipping_fee = self.page.get_by_test_id("shipping-fee")

    def get_lot_name(self):
        self.lot_title.wait_for(state="visible", timeout=10000)
        return self.lot_title.inner_text().strip()

    def get_current_bid(self):
        self.bid_section.wait_for(state="visible", timeout=10000)
        text = self.bid_section.inner_text()
        match = re.search(r"[€$£]\s*[\d,.]+", text)
        return match.group(0).strip() if match else "N/A"

    def get_favourites_count(self):
        try:
            self.favourites_button.wait_for(state="visible", timeout=5000)
            return self.favourites_button.inner_text().strip()
        except Exception:
            return "N/A"
