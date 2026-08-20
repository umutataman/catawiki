from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.results_container = self.page.get_by_test_id("SearchResults")
        self.lot_cards = self.page.locator("[data-testid^='lot-card-container-']")
        self.object_count = self.page.get_by_test_id("object-amount")
        self.filters = self.page.get_by_test_id("sticky-filters")
        self.pagination = self.page.get_by_test_id("pagination")
        self.save_search_button = self.page.get_by_test_id("save-your-search_button")

    def get_lots_count(self):
        self.lot_cards.first.wait_for(state="visible", timeout=15000)
        return self.lot_cards.count()

    def get_result_count_text(self):
        self.object_count.wait_for(state="visible", timeout=10000)
        return self.object_count.inner_text().strip()

    def click_lot_by_index(self, index):
        self.lot_cards.first.wait_for(state="visible", timeout=10000)
        self.lot_cards.nth(index).click()
        self.page.wait_for_load_state("domcontentloaded")
        from pages.lot_details_page import LotDetailsPage
        return LotDetailsPage(self.page)
