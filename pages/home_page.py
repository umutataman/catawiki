from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_input = self.page.get_by_test_id("search-field").first
        self.featured_objects = self.page.get_by_test_id("home-featured-objects")
        self.all_auctions_tab = self.page.get_by_test_id("all-auctions-tab")

    def open(self):
        self.navigate()
        return self

    def search_for(self, keyword):
        self.dismiss_cookies()
        self.search_input.wait_for(state="visible", timeout=10000)
        self.search_input.fill(keyword)
        self.search_input.press("Enter")
        self.page.wait_for_url("**/s?**", timeout=10000)

    def click_category_tab(self, category_id_str):
        self.dismiss_cookies()
        cat = self.page.get_by_test_id(category_id_str)
        cat.wait_for(state="visible", timeout=5000)
        cat.click()
        self.page.wait_for_load_state("domcontentloaded")
        
    def goto_all_auctions(self):
        self.dismiss_cookies()
        self.all_auctions_tab.wait_for(state="visible", timeout=5000)
        self.all_auctions_tab.click()
        self.page.wait_for_url("**/a**", timeout=10000)
