from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


def test_search_no_exact_results(page):
    """
    Negative Scenario:
    Search for a completely invalid term and verify the 
    application gracefully handles it with a "No exact results" message.
    """
    home = HomePage(page).open()
    home.search_for("thisisacompletelyinvalidsearchterm")

    # The site falls back to related objects, but should show an explicit empty state message
    page.wait_for_load_state("domcontentloaded")
    
    # Assert the fallback message is visible on the page
    no_results_message = page.get_by_text("No exact results")
    assert no_results_message.is_visible(timeout=10000), "Should display a message indicating no exact matches were found"


def test_unauthenticated_save_search(page):
    """
    Negative / Authorization Scenario:
    Attempt to use an authenticated feature (Save search) while logged out,
    and verify the application prompts the user to sign in.
    """
    home = HomePage(page).open()
    home.search_for("Train")

    results = SearchResultsPage(page)
    results.save_search_button.wait_for(state="visible", timeout=10000)
    
    # Click save search while unauthenticated
    results.save_search_button.click()
    
    # Verify the login/registration modal intercepts the action
    login_modal_text = page.get_by_text("Sign in or create an account").first
    assert login_modal_text.is_visible(timeout=10000), "Authentication modal should appear when attempting to save search"
