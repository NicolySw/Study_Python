import runner_and_tournament as rnt
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        vs = {'Усэйн': 10, 'Андрей': 9, 'Ник': 3}
        self.runners = {n: rnt.Runner(name=n, speed=v) for n, v in vs.items()}

    @classmethod
    def tearDownClass(cls):
        print(cls.all_result)
        for k, v in cls.all_result.items():
            print("0-0")
            print(f'{k}: {v}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament(self):
        tour = rnt.Tournament(90, self.runners['Усэйн'], self.runners['Ник'])
        all_result = tour.start()
        self.assertTrue(all_result[2], self.runners['Ник'])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        tour = rnt.Tournament(90, self.runners['Андрей'], self.runners['Ник'])
        all_result = tour.start()
        self.assertTrue(all_result[2], self.runners['Ник'])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        tour = rnt.Tournament(90, self.runners['Усэйн'], self.runners['Андрей'], self.runners['Ник'])
        all_result = tour.start()
        self.assertTrue(all_result[3], self.runners['Ник'])

    if __name__ == '__main__':
        unittest.main()
