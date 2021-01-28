import unittest

class TestStringMethods(unittest.TestCase):
    # setUp 和 tearDown 是在每条测试用例前后分别调用g



    def setUp(self) -> None:
        print("setup")

    # after testcases
    def tearDown(self) -> None:
        print("tearDown")
    # setUpClass 和 tearDownClass是在整个类的前后分别调用的方法
    @classmethod
    def setUpClass(cls) -> None:
        print("setUp class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDown Class")

    def test_abc(self):
        print("test.abc")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        print("test_upper")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
