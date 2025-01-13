import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = Runner('Walker')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        runner = Runner('Runner')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner = Runner('Challenge')
        walker = Runner('Walker')
        for i in range(10):
            walker.walk()
            runner.run()
        self.assertNotEqual(walker.distance, runner.distance)




