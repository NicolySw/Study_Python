import calk
import unittest


class CalkTest(unittest.TestCase):
    def setUp(self):  # подключается перед каждым тестированием
        print("setup")

    @classmethod  # выполняется один раз при запуске
    def setUpClass(cls):
        print("MegaSetup")

    def tearDown(self):  # запускается после любого теста
        pass

    @classmethod  # после всех тестов запускается
    def tearDownClass(cls):
        pass

    def test_add(self):
        """
        Test for add function in calculator
        :return:
        """
        self.assertEqual(calk.add(10, 20), 30)

    def test_sub(self):
        self.assertEqual(calk.sub(5, 3), 2)

    def test_test(self):
        self.assertIn("s", "ssdf")


if __name__ == '__main__':
    unittest.main()
