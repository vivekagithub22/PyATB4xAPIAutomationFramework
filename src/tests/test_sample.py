import pytest
import allure

@allure.title("sample testcase")
def test_sample():
    assert True == True





# Run command-
# pytest -s src/tests/test_sample.py --alluredir=allure_result

# allure serve allure_result

