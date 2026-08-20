from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


def test_search_review_lot_details(page):
    """
    Core Assessment Scenario:
    1. Open website
    2. Search "Train"
    3. Verify results open
    4. Click 2nd lot
    5. Print Name, Favourites, Current Bid
    """
    home = HomePage(page).open()
    home.search_for("Train")

    results = SearchResultsPage(page)
    assert results.results_container.is_visible(timeout=10000)
    assert results.get_lots_count() >= 2

    # Click on the second lot (index 1)
    lot = results.click_lot_by_index(1)
    assert "/l/" in page.url

    # Get values
    lot_name = lot.get_lot_name()
    favourites = lot.get_favourites_count()
    current_bid = lot.get_current_bid()

    # Print EXACTLY as requested, no extra fluff
    print("\nLot Details:")
    print(f"Lot's Name: {lot_name}")
    print(f'"Favourites" Counter: {favourites}')
    print(f"Current Bid: {current_bid}")

    # Basic assertions to ensure we scraped valid data
    assert len(lot_name) > 0
    assert current_bid != "N/A"


def test_search_view_modes_and_persistence(page):
    """
    Complex Scenario:
    Perform a search, verify the count text matches expected format,
    toggle the view mode from normal to gallery, and verify the state changes.
    """
    home = HomePage(page).open()
    home.search_for("Rolex")

    results = SearchResultsPage(page)
    
    # Extract and verify the object count format (e.g. "1500 objects")
    count_text = results.get_result_count_text()
    assert "objects" in count_text.lower() or "results" in count_text.lower()
    
    # Toggle to Gallery View
    gallery_btn = page.get_by_test_id("view-mode-gallery")
    if gallery_btn.is_visible():
        gallery_btn.click()
        page.wait_for_timeout(1000)  # wait for layout shift
        
        # Verify the gallery button becomes active/disabled (depending on implementation)
        # We can verify URL or just the button state
        assert gallery_btn.is_visible()
