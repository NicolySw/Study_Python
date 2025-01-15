import unittest
import RunnerTest
import TournamentTest

calcST = unittest.TestSuite()
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest.RunnerTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcST)
