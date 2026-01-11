# SauceDemo Automation Tests

This repository contains automation tests for (https://www.saucedemo.com/) using Selenium, Pytest, and Allure.  

Test scenarios:

- **Q1:** Login with `locked_out_user` and verify the error message.
- **Q2:** Login with `standard_user`, add products to the cart, complete checkout, verify the order, then reset app state and log out.
- **Q3:** Login with `performance_glitch_user`, filter products, add to cart, complete checkout, verify order, then reset app state and log out.

---

## Installation

1. Make sure **Python 3.14.2** is installed on your system.  

2. Required libraries for running the tests:

pip install selenium
pip install pytest
pip install allure-pytest
pip install webdriver-manager

## Project Structure

tests/

   -test_1_locked.py           # Q1: locked_out_user test
   -test_2_standard.py         # Q2: standard_user test
   -test_3_performance.py      # Q3: performance_glitch_user test
  
pages/

  -login.py
  -inventory.py
  -cart.py
  -checkout.py

## Test:

Individual tests:

python -m pytest tests/test_1_locked

python -m pytest tests/test_2_standard

python -m pytest tests/test_3_performance


Sequential tests:

python -m pytest


Sequential tests with allure report:

python -m pytest --alluredir=allure-results

