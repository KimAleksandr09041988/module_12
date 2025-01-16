from runner import Runner, Tournament
from unittest import TestCase

class RunnerTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(cls):
        cls.runner_1 = Runner('Усэйн', 10)
        cls.runner_2 = Runner('Андрей', 9)
        cls.runner_3 = Runner('Ник',3)

    @classmethod
    def tearDownClass(cls):
        for _, j in cls.all_results.items():
            print(j)

    def test_1(cls):
        dict_ = Tournament(90, cls.runner_1, cls.runner_3).start()
        for i, j in dict_.items():
            dict_[i] = j.name
        cls.all_results[str(len(cls.all_results))] = dict_
        cls.assertTrue(cls.all_results[str(len(cls.all_results) - 1)]
              [len(cls.all_results[str(len(cls.all_results) - 1)])] == 'Ник')

    def test_2(cls):
        dict_ = Tournament(90, cls.runner_2, cls.runner_3).start()
        for i, j in dict_.items():
            dict_[i] = j.name
        cls.all_results[str(len(cls.all_results))] = dict_
        cls.assertTrue(cls.all_results[str(len(cls.all_results) - 1)]
              [len(cls.all_results[str(len(cls.all_results) - 1)])] == 'Ник')

    def test_3(cls):
        dict_ = Tournament(90, cls.runner_1,cls.runner_2, cls.runner_3).start()
        for i, j in dict_.items():
            dict_[i] = j.name
        cls.all_results[str(len(cls.all_results))] = dict_
        cls.assertTrue(cls.all_results[str(len(cls.all_results) - 1)]
              [len(cls.all_results[str(len(cls.all_results) - 1)])] == 'Ник')

if __name__ == '__main__':
    RunnerTest()
