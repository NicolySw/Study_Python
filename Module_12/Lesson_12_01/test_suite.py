import unittest
import test_calc_2
import test_new_calk


calcST = unittest.TestSuite()
calcST.addTests(unittest.TestLoader().loadTestsFromTestCase(test_calc_2.CalkTest))
calcST.addTests(unittest.TestLoader().loadTestsFromTestCase(test_new_calk.NewTestCalc))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcST)
