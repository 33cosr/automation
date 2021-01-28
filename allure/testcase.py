import pytest
import allure

TESE_CASE_LINK = "https://www.baidu.com"


@allure.testcase(TESE_CASE_LINK, "Test case title")
def test_with_testcase_link():
    pass

# pytest --alluredir=./results
# allure serve ./results
# allure generate ./results -o allure_jenny_report