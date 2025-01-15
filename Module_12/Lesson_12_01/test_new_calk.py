import unittest
import calk

class NewTestCalc(unittest.TestCase):

    def test_sqrt(self):
        self.assertEqual(calk.sqrt(4), 2)

    def test_pow(self):
        self.assertEqual(calk.pow(3, 3), 27)



