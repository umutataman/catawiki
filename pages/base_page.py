import os

BASE_URL = os.getenv("BASE_URL", "https://www.catawiki.com/en")


class BasePage:
    def __init__(self, page):
        self.page = page
        self.base_url = BASE_URL

    def navigate(self, path=""):
        url = f"{self.base_url.rstrip('/')}/{path.lstrip('/')}" if path else self.base_url
        self.page.goto(url, wait_until="domcontentloaded")
        self.dismiss_cookies()

    def dismiss_cookies(self):
        try:
            accept_btn = self.page.get_by_test_id("uc-footer").get_by_text("Accept All")
            if accept_btn.is_visible(timeout=3000):
                accept_btn.click()
                self.page.wait_for_timeout(500)
        except Exception:
            pass
