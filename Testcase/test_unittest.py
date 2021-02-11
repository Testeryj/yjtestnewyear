import unittest
class Demo01(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")
    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")


    def test_case01(self):
        print("testcase01")
        self.assertEqual(2, 2, "判断相等")
        self.assertIn('h', 'this')

    def test_case02(self):
        print("testcase02")
        self.assertEqual(3, 3, "判断不相等")
        # self.assertIn('h', 'this')

    @unittest.skipIf(1+1==2,"跳过这条用例")
    def test_case03(self):
        print("testcase03")
        self.assertEqual(10, 9, "判断不相等")
        # self.assertIn('h', 'this')



class Demo02(unittest.TestCase):
    def test_case03(self):
        print("testcase03")
        self.assertEqual(9, 9, "判断相等")
        self.assertIn('h', 'this')

    def test_case04(self):
        print("testcase04")
        self.assertEqual(10, 10, "判断不相等")
        # self.assertIn('h', 'this')

class Demo02(unittest.TestCase):
    def test_case05(self):
        print("testcase05")
        self.assertEqual(9, 9, "判断相等")
        self.assertIn('h', 'this')

    def test_case06(self):
        print("testcase06")
        self.assertEqual(10, 10, "判断不相等")
                # self.assertIn('h', 'this')

if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(Demo01("test_case03"))
    # suite.addTest(Demo02("test_case01"))
    # unittest.TextTestRunner().run(suite)


    suite = unittest.TestLoader().loadTestsFromTestCase(Demo01)
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Demo02)
    suiteall = unittest.TestSuite([suite, suite1])
    unittest.TextTestRunner().run(suiteall)




































