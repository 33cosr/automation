import unittest

class Search:

    def search_fun(self):
        print("search")
        return True
class TestSearch2(unittest.TestCase):
    def test_case1(self):
        print("TestSearch2 Class case1")

class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        search = Search()
        cls.search = search.search_fun()

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_search1(self):
        print("test search1")
        assert True == self.search

    def test_search2(self):
        print("test search2")
        assert True == self.search

    def test_search3(self):
        print("test search3")
        assert True == self.search

    def test_equal(self):
        print("equal")
        self.assertEqual(1, 1, 'judge 1 = 1')

    def test_notequal(self):
        print("nequal")
        # self.assertNotEqual(1, 2, "judage 1!=2")
        self.assertTrue(1==1,"verfify")

if __name__ == '__main__':
    # method 1 ,excute all unittest testcases
    # unittest.main()

    # method 2 use testsuite
    # create testsuite
    # suite = unittest.TestSuite()
    # suite.addTest(TestSearch("test_search1"))
    # suite.addTest(TestSearch("test_search3"))
    # unittest.TextTestRunner().run(suite)


    # method 3 test multiple classes
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSearch2)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)
