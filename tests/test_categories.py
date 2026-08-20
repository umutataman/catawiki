from pages.home_page import HomePage


def test_browse_jewellery_category(page):
    """
    Test navigation to a specific category (Jewellery) directly from the homepage tab.
    Verifies URL routing and category landing page properties.
    """
    home = HomePage(page).open()
    
    # Category 714 is Jewellery
    home.click_category_tab("category-714")
    
    # Verify the route
    assert "/c/714" in page.url
    assert "Jewellery" in page.title()


def test_browse_watches_category(page):
    """
    Test navigation to the Watches category (299) and ensure 
    core layout elements like the search field remain accessible.
    """
    home = HomePage(page).open()
    
    # Category 299 is Watches
    home.click_category_tab("category-299")
    
    # Verify the route
    assert "/c/299" in page.url
    assert "Watches" in page.title()
    
    # Verify the search field persists on category pages
    assert page.get_by_test_id("search-field").first.is_visible()
