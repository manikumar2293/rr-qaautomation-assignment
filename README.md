# RR QA Automation Assignment

## Overview

This project is a **QA automation suite** for the demo website [TMDb Discover](https://tmdb-discover.surge.sh/).  
The website simulates a movie and TV show listing platform similar to IMDb.  

The suite covers:

- API testing using `movies.json`  
- UI testing using Selenium  
- Logging of all steps and failures  
- HTML report generation with `pytest-html`  
- Handling filters, pagination, and negative scenarios  

---

## Project Structure


---

## Testing Strategy

### 1. API Testing

- Used `movies.json` to simulate TMDb API responses.  
- Verified:
  - JSON structure and keys: `id`, `title`, `release_date`, `vote_average`, `genre_ids`, `poster_path`, etc.
  - Rating and genre filters
  - Pagination (page number and total pages)
  - Edge cases like empty results or invalid filters
- Handled network issues with **retry mechanism** and **timeouts**.

**Example validation**:

- Check all movies have `title` and `release_date`
- Verify `vote_average` is within 0–5
- Verify genres include expected IDs (e.g., 16 = Animation)

### 2. UI Testing (Selenium)

- Verified filters and interaction:
  - **Categories:** Popular, Trending, Newest, Top Rated  
  - **Type:** Movies or TV Shows  
  - **Year of Release:** From earliest to latest  
  - **Rating:** Minimum and maximum values  
  - **Genre:** Animation, Action, Comedy, etc.  
- Verified **pagination**
- Checked **page refresh / slug URLs**
- **Screenshots** captured for any failure

**Example UI assertions**:

- Clicking **Popular** loads first page correctly
- Filter by **Genre=16 (Animation)** only shows Animation movies
- Page 2 shows correct movie titles from `movies.json`

---

## Logging

- Used Python `logging` module.
- Logs include:
  - Start/end of each test
  - Steps performed (API calls, UI actions)
  - Errors and exceptions
- Example:
2025-09-25 10:00:01 INFO: Starting API tests
2025-09-25 10:00:05 INFO: Verified movie "Hocus Pocus, Alfie Atkins!" rating 4.0
2025-09-25 10:00:10 INFO: Starting UI tests - Popular category
2025-09-25 10:00:15 ERROR: Page failed to load on /popular slug


---

## HTML Reporting

- Reports generated using **pytest-html**  
- Includes:
  - Summary of all tests
  - Pass/Fail status
  - Screenshot attachments for failed tests
  - Execution time
- Example:

Test Suite: TMDb QA Automation
Total tests: 09
Passed: 07
Failed: 02
Skipped: 0


---

## Test Design Techniques

- **Data-Driven Testing:** Used `movies.json` for API validation  
- **Parameterized Tests:** Different categories, genres, years  
- **Page Object Model (POM):** Maintainable UI automation (can be extended)  
- **Retries & Timeout Handling:** To handle slow network/API responses  
- **Negative Scenarios:**  
  - Accessing broken slug URLs  
  - Pagination beyond last page  
  - Invalid filter combinations  

---

## Defects Found

- Slug URLs (e.g., `/popular`) sometimes fail on refresh  
- Pagination broken for last few pages  
- Some rating/genre filters return empty results  
- UI occasionally fails on slow network without retries

---

name: TMDb QA Automation CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install Dependencies
        run: pip install -r requirements.txt
      - name: Run API & UI Tests
        run: pytest test_suite/ --html=report.html -v
      - name: Upload Artifacts
        uses: actions/upload-artifact@v3
        with:
          name: test-report
          path: report.html