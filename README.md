# QA Automation Framework – UI & API Testing {Python + Playwright}

## 📌 Project Overview

This project demonstrates an end-to-end **Automation Testing Framework** covering both:

✅ UI Automation using Playwright  
✅ API Automation using Requests  
✅ Parallel Execution  
✅ Allure Reporting  
✅ Modern Synchronization Strategies  

The framework follows scalable automation practices similar to enterprise Product-based companies.

---

# 🧰 Technology Stack

| Category | Tool |
|-----------|------|
| Language | Python 3 |
| IDE | VS Code |
| OS | Mac OS |
| UI Automation | Playwright |
| API Automation | Requests |
| Test Runner | Pytest |
| Reporting | Allure |
| Parallel Execution | pytest-xdist |
| Design Pattern | Page Object Model |

---

# ⚙️ Environment Setup (From Scratch)

---

## ✅ Step 1 – Install VS Code

Download and install:

https://code.visualstudio.com/

Recommended Extensions:
- Python
- Playwright Test for VSCode

---

## ✅ Step 2 – Install Python

Download Python (3.9+):

https://www.python.org/downloads/

Verify installation:

```bash
python3 --version

✅ Step 3 – Clone Repository
git clone <https://github.com/AvinashGandi-LEAD-SDET-Automation/qa-automation-framework-playwright-python.git>

cd qa-automation-framework-playwright-python

✅ Step 4 – Create Virtual Environment and activate it

python3 -m venv env 
source env/bin/activate

✅ Step 5 – Upgrade pip
python -m pip install --upgrade pip

✅ Step 6 – Install Project Dependencies
pip install -r requirements.txt

✅ Step 7 – Install Playwright Browsers
playwright install

This installs:  Chromium/Firefox/WebKit

📁 Project Structure

qa-automation-framework-playwright-python
│
├── .pytest_cache/                 # Pytest execution cache
│
├── api/                           # API automation layer
│   ├── __init__.py
│   ├── .gitkeep
│   └── products_client.py         # Products API client
│
├── config/                        # Configuration files (env/test configs)
│
├── data/                          # Test data files
│
├── env/                           # Python virtual environment
│
├── pages/                         # Page Object Model (UI Layer)
│   ├── __init__.py
│   ├── login_page.py
│   ├── product_page.py
│   └── cart_page.py
│
├── reports/                       # Generated execution reports
│
├── tests/                         # Test suites
│   │
│   ├── API/                       # API test cases
│   │   └── test_products_api.py
│   │
│   └── UI/                        # UI test cases
│       ├── login_page_test.py
│       ├── product_page_test.py
│       ├── cart_page_test.py
│       └── async_page_test.py
│
├── utils/                         # Utility helpers
│   └── .gitkeep
│
├── .gitignore
├── conftest.py                    # Pytest fixtures & hooks
├── pytest.ini                     # Pytest configuration
├── requirements.txt               # Project dependencies
├── README.md                      # Project documentation
└── sync_test.txt                  # Sample/test reference file

✅ UI Automation
https://www.saucedemo.com/
Covered Scenarios
___________________

Login validation
Product listing validation
Add product to cart
Cart verification
Navigation validation
Playwright waiting strategies
Waiting Strategies Used
No hard sleeps (time.sleep()).
Implemented:
Element visibility waits
Network idle waits
URL waits
Playwright auto-wait mechanism

✅ API Automation

https://dummyjson.com/products

Test Coverage

✔ GET all products
✔ GET product by ID
✔ Negative API validation

Validations include:
Status codes
Response schema
Data type checks
Error handling

⚡ Parallel Execution
Parallel execution enabled using pytest-xdist.
Run tests in parallel:

pytest -n 4 {no of threads we can give}

📊 Allure Reporting

Generate Test Results..
pytest --alluredir=allure-results

Open Report 
allure serve allure-results

Report provides
Execution summary
Test steps
Pass/Fail status
Failure analysis

▶ Running Tests
Run All Tests
pytest -v

Run UI Tests Only
pytest -m ui

Run API Tests Only
pytest -m api

Run total login page Tests
pytest tests/UI/login_page_test.py

Parallel + Allure 
pytest -n auto --alluredir=allure-results

✅ Framework Design Highlights

Page Object Model (POM)
Reusable fixtures
Parallel-safe browser contexts
API client abstraction
Maintainable structure
Enterprise-ready design

🚀 Future Improvements

CI/CD integration
Docker execution
Environment configuration
Retry mechanism
API schema validation

🚀 CI Pipeline Integration Approach {optional request}

## 🚀 CI/CD Integration Strategy

This automation framework is designed to be easily integrated into a Continuous Integration (CI) pipeline such as **Jenkins**, **GitHub Actions**, **GitLab CI**, or **Azure DevOps**.

### ✅ Integration Approach

1. **Source Control Trigger**
   - Pipeline execution is triggered automatically on:
     - Pull Requests
     - Code commits
     - Scheduled regression runs

2. **Environment Setup Stage**
   - Install Python runtime
   - Create virtual environment
   - Install dependencies using:
     ```bash
     pip install -r requirements.txt
     ```
   - Install Playwright browsers:
     ```bash
     playwright install
     ```

3. **Test Execution Stage**
   - Execute tests in parallel for faster feedback:
     ```bash
     pytest -n auto --alluredir=allure-results
     ```

4. **Reporting Stage**
   - Generate Allure reports:
     ```bash
     allure generate allure-results --clean -o allure-report
     ```
   - Publish reports as pipeline artifacts for visibility.

5. **Failure Handling**
   - Failed tests automatically capture logs and screenshots.
   - Reports provide detailed failure analysis for debugging.

---

### ✅ Recommended Pipeline Flow
Code Commit
↓
CI Trigger
↓
Environment Setup
↓
Install Dependencies
↓
Run UI + API Tests (Parallel)
↓
Generate Allure Report
↓
Publish Test Results

✅ Future CI Enhancements

Docker-based execution environment
Scheduled nightly regression runs
Environment-based execution (QA/UAT/Prod)
Automated notification integration (Slack/Email)
Test result trend analysis

## 📊 Allure Report (Execution Results)

The automation framework integrates **Allure Reporting** to provide detailed execution insights including test steps, execution status, and failure analysis.
⚠️ **Note:**  
If the Allure report preview image is not visible due to GitHub rendering limitations, please use the below link to view the execution report directly:

🔗 **Allure Report Link:**  
https://raw.githubusercontent.com/AvinashGandi-LEAD-SDET-Automation/personal-drive/main/photos/allurereport.png


👨‍💻 Author
Avinash Gandi
Lead SDET
