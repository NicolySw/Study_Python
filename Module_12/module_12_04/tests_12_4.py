import logging
import unittest
from rt_with_exceptions import Runner


class RunnerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename='runner_tests.log', filemode='w', level=logging.INFO, encoding='utf-8',
                            format='%(asctime)s | %(levelname)s | %(message)s')

    def test_walk(self):
        try:
            walker = Runner('Walker', -1)
            for i in range(10):
                walker.walk()
            self.assertEqual(walker.distance, 10)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner = Runner(222, 5)
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO, filemode='w', filename="py.log",
    #                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    unittest.main()