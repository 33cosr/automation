import pytest
import allure

def test_with_no():
    pass


@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)
class TestSeverity(object):

    def test_inside_the_nore_severity_test_class(self):
        pass


