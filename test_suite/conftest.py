import pytest
import json
import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

MOVIES_FILE = "movies.json"

# ----------------------
# Logging setup
# ----------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("movies_test.log"),
        logging.StreamHandler()
    ]
)

# ----------------------
# Load movies fixture
# ----------------------
@pytest.fixture(scope="session")
def movies():
    if os.path.exists(MOVIES_FILE):
        with open(MOVIES_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            logging.info(f"✅ Loaded {len(data.get('results', []))} movies from {MOVIES_FILE}")
            return data.get("results", [])
    else:
        pytest.exit(f"❌ {MOVIES_FILE} not found!")

# ----------------------
# Selenium browser fixture
# ----------------------
@pytest.fixture(scope="session")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode for CI or quick tests
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Setup ChromeDriver using webdriver-manager 3.x
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    yield driver
    driver.quit()
