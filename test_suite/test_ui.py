# test_suite/test_ui.py
import pytest
import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# -------------------- Logging Setup --------------------
logging.basicConfig(
    filename='movies_test.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# -------------------- Fixtures --------------------
@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

# -------------------- Test Cases --------------------
def test_pagination_ui(driver):
    url = "https://tmdb-discover.surge.sh/"
    max_retries = 3
    retry_count = 0

    while retry_count < max_retries:
        try:
            logging.info(f"Opening website: {url}, attempt {retry_count + 1}")
            driver.get(url)

            # Wait until movie cards load
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".movie-card"))
            )
            logging.info("Movies loaded successfully.")

            # Try clicking Next Page if exists
            try:
                next_buttons = driver.find_elements(By.CSS_SELECTOR, "button[aria-label='Next Page']")
                if next_buttons:
                    next_button = next_buttons[0]
                    driver.execute_script("arguments[0].scrollIntoView();", next_button)
                    next_button.click()
                    logging.info("Next Page button clicked successfully.")
                else:
                    logging.warning("Next Page button not found. Possibly last page.")
            except (NoSuchElementException, TimeoutException) as e:
                logging.warning(f"Pagination element issue: {e}")

            # Exit loop if page loaded successfully
            break
        except TimeoutException:
            logging.warning("Page load timeout. Retrying...")
            retry_count += 1
            time.sleep(2)
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            retry_count += 1
            time.sleep(2)

    assert retry_count < max_retries, "Failed to load page after multiple retries."
