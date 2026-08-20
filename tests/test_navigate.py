from pages.home_page import HomePage


def test_header_navigation_links(page):
    """
    Verify global header navigation items are present and 
    validate external/internal routing for the Help center.
    """
    home = HomePage(page).open()
    
    # Test 'How it works' presence
    how_it_works = page.get_by_test_id("header-how-it-works-button")
    how_it_works.wait_for(state="visible", timeout=10000)
    assert how_it_works.is_visible()
    
    # Test 'Help' center navigation
    help_btn = page.get_by_test_id("header-help-button")
    help_btn.click()
    
    # Wait for the help center route
    page.wait_for_url("**/help**")
    assert "Help" in page.title()


def test_all_auctions_feed(page):
    """
    Navigate from the homepage feed directly into the comprehensive 
    'All Auctions' page and verify its unique layout container.
    """
    home = HomePage(page).open()
    
    home.goto_all_auctions()
    
    # Verify the master auctions route and unique page container
    assert "/a" in page.url
    assert page.get_by_test_id("all-auctions-page").is_visible(timeout=10000)
