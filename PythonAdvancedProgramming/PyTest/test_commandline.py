# ============================
# PYTEST COMMAND CHEAT SHEET
# ============================

# Run all test cases in a file
# pytest test_case.py

# Run tests with verbose output
# pytest -v test_case.py
# pytest -vv test_case.py

# Show print statements in console
# pytest -s test_case.py

# Verbose + show print statements
# pytest -vv -s test_case.py

# Generate HTML report
# pytest test_case.py --html=test_case_report.html

# Run tests in parallel (requires pytest-xdist)
# pytest test_parallel.py -n 4 --html=report.html

# Run only smoke test cases
# pytest -m smoke

# Run tests marked as both smoke AND api
# pytest -m "smoke and api"

# Run tests marked as smoke OR api
# pytest -m "smoke or api"

# Run all tests except regression
# pytest -m "not regression"

# Run test cases whose names contain 'login'
# pytest -k login

# Run only the last failed test cases
# pytest -lf

# Run all tests inside a folder
# pytest tests/api/

# Run a specific test function inside a file
# pytest login.py::test_valid_login

# Stop execution after first failure
# pytest -x
