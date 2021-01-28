import pytest
import allure

@allure.feature("search module feature")
class TestSearch():
    def test_case1(self):
        print("testcase1")

    def test_case2(self):
        print("testcase2")



@allure.feature("login module feature")
class TestLogin():
    @allure.story("login success story")
    @allure.title("login success title")
    def test_login_success(self):
        print("this is login: testcase, login success")
        with allure.step("step 1: open app"):
            print("open app")

        with allure.step("step 2: enter login"):
            print("enter login page")

        with allure.step("step 3: input username and password"):
            print("input input username and password")

        pass

    @allure.story("login fail story")
    @allure.title("login fail title")
    def test_login_fail(self):
        print("this is login: testcase, login fail")
        pass
