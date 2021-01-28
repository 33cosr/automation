import pytest


def func(x):
    return x + 1


@pytest.mark.parametrize('a,b', [(1, 2),
                                 (10, 20),
                                 ('a', 'a1'),
                                 (3,4),
                                 (5,6)])
def test_answer(a, b):
    assert func(a) == b


def test_answer1():
    assert func(4) == 5

@pytest.fixture()
def login():
    print("login operation")
    username = "jenny"
    return username


class TestDemo:
    def test_a(self, login): # 方法名字代表返回结果
        # print("\na")
        print(f"a  username = {login}")

    def test_b(self):
        print("b")

    def test_c(self, login):
        print(f"c user name = {login}")

#  pytest.main(['test_a.py']) python inteerpreter
#  pytest.main(['test_a.py::TestDemo','-v'])
#  和命令行 pytest 类似
