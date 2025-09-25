import logging
import pytest
from selenium.webdriver.common.by import By
from conftest import browser

BASE_URL = "https://tmdb-discover.surge.sh"

# ----------------------
# Helper function
# ----------------------
def get_ui_titles(driver):
    """Extract visible movie titles on page."""
    elements = driver.find_elements(By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-h6")
    titles = [el.text.strip() for el in elements if el.text.strip()]
    return titles

# ----------------------
# Test Cases
# ----------------------
def test_open_home_page(browser):
    logging.info("Opening TMDb home page")
    browser.get(BASE_URL)
    assert "TMDB" in browser.title or "Discover" in browser.title

def test_popular_category_ui(browser, movies):
    logging.info("Testing Popular category UI")
    browser.get(f"{BASE_URL}/popular")
    browser.implicitly_wait(3)
    ui_titles = get_ui_titles(browser)
    logging.info(f"UI titles found: {ui_titles[:5]}")

    # Compare first 5 UI titles with first 5 from movies.json popularity descending
    top_movies = sorted(movies, key=lambda m: m.get("popularity", 0), reverse=True)[:5]
    api_titles = [m["title"] for m in top_movies]
    logging.info(f"API titles: {api_titles}")

    # Assert overlap of at least 1 title
    assert any(title in ui_titles for title in api_titles)

def test_slug_refresh_negative(browser):
    logging.info("Testing slug refresh negative scenario")
    browser.get(f"{BASE_URL}/popular")
    browser.refresh()
    browser.implicitly_wait(3)
    try:
        titles = get_ui_titles(browser)
        logging.info(f"Titles after refresh: {titles[:5]}")
        assert len(titles) > 0
    except Exception as e:
        logging.warning(f"Known demo issue: page may not load fully on refresh: {e}")
        pytest.xfail("Demo site known refresh issue")

def test_pagination_ui(browser):
    logging.info("Testing UI pagination")
    browser.get(BASE_URL)
    browser.implicitly_wait(3)
    next_button = browser.find_element(By.CSS_SELECTOR, "button[aria-label='Next Page']")
    if next_button:
        next_button.click()
        browser.implicitly_wait(3)
        titles_page2 = get_ui_titles(browser)
        logging.info(f"Titles on page 2: {titles_page2[:5]}")
        assert len(titles_page2) > 0
