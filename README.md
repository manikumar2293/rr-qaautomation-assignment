## TMDB QA Automation Assignment

## Repository: rr-qaautomation-assignment(https://github.com/manikumar2293/rr-qaautomation-assignment.git)

Demo Website: TMDB Discover(https://tmdb-discover.surge.sh/)

## Project Overview

This project is a QA automation assignment for the TMDB Discover demo website. It demonstrates:

UI Testing: Validates categories, filters, and pagination using Selenium WebDriver.

API Testing: Verifies API endpoints, JSON structure, and status codes using Python requests.

Logging & Reporting: Captures logs for debugging and generates HTML reports for test execution results.

Documentation: Includes test plan, strategy, test cases (Excel), and scenarios in Word format.

Purpose: Ensure filtering, pagination, and data displayed on the website match the API responses and meet functional requirements.

## Features Covered - Filtering Options

- Categories: Popular, Trending, Newest, Top Rated

- Titles

- Type: Movies or TV Shows

- Year of Release

- Rating

- Genre

- Pagination

- API Validation

- Status codes

- JSON structure and data integrity

- Known Demo Issues (for negative testing)

- Refreshing/accessing the page via slugs may fail (e.g., /popular)

- Pagination may fail on the last few pages

## Project Structure

## RR_QA_AUTOMATION/
├─ docs/
│  ├─ Test_Plan.docx
│  ├─ Test_Strategy.docx
│  ├─ Test_Cases.xlsx
│  └─ Test_Scenarios.docx
├─ movies.json                  # Sample API response data
├─ README.md                     # Project documentation
├─ requirements.txt              # Python dependencies
├─ movies_test.log               # Execution logs
├─ report.html                   # Pytest HTML test report
└─ test_suite/
   ├─ test_api.py                # API tests
   └─ test_ui.py                 # UI Selenium tests


## Setup Instructions

1. ## Clone the repository
   git clone https://github.com/yourusername/rr-qaautomation-assignment.git
   cd rr-qaautomation-assignment

2. ## Create virtual environment
   python -m venv .venv
   .\.venv\Scripts\activate   # Windows

3. ## Install dependencies
   pip install -r requirements.txt

4. ## Ensure Chrome Browser is installed (for Selenium WebDriver tests)

## How to Run Tests
## UI Tests

pytest test_suite/test_ui.py --html=ui_report.html --self-contained-html

## API Tests

pytest test_suite/test_api.py --html=api_report.html --self-contained-html

Logs will be generated in movies_test.log

HTML reports will be generated in ui_report.html and api_report.html

## Logging

All test steps, API calls, and errors are logged with timestamps in movies_test.log.

Helps debug test failures and track execution history.


## Documentation

All QA documentation is available in the docs/
 folder:

Test_Plan.docx
 – Overall plan and scope

Test_Strategy.docx
 – Testing approach and automation strategy

Test_Cases.xlsx
 – Detailed test cases with steps and expected results

Test_Scenarios.docx
 – High-level testing scenarios

## Defects Found / Negative Testing

Refreshing the page via category slugs sometimes fails.

Last few pagination pages may not load properly.

API occasionally times out (network-related; handled in test suite with retries).
