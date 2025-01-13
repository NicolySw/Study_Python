import calk
import unittest


class CalkTest(unittest.TestCase):
    def test_add(self):
        """
        Test for add function in calculator
        :return:
        """
        self.assertEqual(calk.add(10, 20), 30)

    def test_sub(self):
        self.assertEqual(calk.sub(5, 3), 2)


if __name__ == '__main__':
    unittest.main()


