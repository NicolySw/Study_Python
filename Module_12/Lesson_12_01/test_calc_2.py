import calk
import unittest
import random


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

    @unittest.skip("skip")
    def test_add(self):
        self.assertEqual(calk.add(10, 20), 30)

    @unittest.skipIf(random.randint(0, 2), "не повезло")
    def test_sub(self):
        self.assertEqual(calk.sub(4, 2), 2)

    def test_test(self):
        self.assertIn("s", "ssdf")


if __name__ == '__main__':
    unittest.main()
