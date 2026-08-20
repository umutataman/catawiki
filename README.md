# Catawiki QA Automation Assessment

Simplified Test Automation Framework using **Python**, **pytest**, **Playwright**, and **uv** built on the **Page Object Model (POM)**.

---

## 📁 Project Structure

```
catawiki_qa_assignment/
├── .github/
│   └── workflows/
│       └── tests.yml            # CI GitHub Actions workflow with uv
├── pages/                       # Page Object Model Layer
│   ├── base_page.py             # Common navigation & cookie consent
│   ├── home_page.py             # Home page actions & search interactions
│   ├── search_results_page.py   # Search results grid & lot selectors
│   └── lot_details_page.py      # Lot details, favourites & bid extraction
├── tests/                       # Test Suite Layer
│   ├── conftest.py              # Playwright fixtures, env defaults, trace retain on failure
│   └── test_search_and_lot.py   # Core Take-Home scenario
├── .env.sample                  # Sample environment variables
├── pyproject.toml               # Project configuration & dependencies for uv
├── requirements.txt             # Pip dependencies
└── README.md                    # Setup & execution instructions
```

---

## ⚡ Quick Start with `uv`

### 1. Install & Setup Environment
```bash
# Sync dependencies with uv
uv sync

# Install Playwright browser binary
uv run playwright install firefox
```

### 2. Run the Test
```bash
# Execute the test with live console output
uv run pytest -s -v

# Generate HTML test report
uv run pytest -s -v --html=report.html --self-contained-html
```

---

## 🔍 Playwright Trace on Failure

When a test fails, a Playwright trace archive is automatically captured and saved under `test-results/<test_name>/trace.zip`.

You can inspect the trace using:
```bash
uv run playwright show-trace test-results/<test_name>/trace.zip
```
