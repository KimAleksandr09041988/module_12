from runner import Runner_1
from runner_and_tournament import Runner_2, Tournament
from unittest import TestCase, skipIf

class RunnerTest(TestCase):
    is_frozen = False

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        obj = Runner_1('test')
        for _ in range(10):
            obj.walk()
        self.assertEqual(obj.distance, 50)

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        obj = Runner_1('test')
        for _ in range(10):
            obj.run()
        self.assertEqual(obj.distance, 100)

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        obj_1 = Runner_1('test_1')
        obj_2 = Runner_1('test_2')
        for _ in range(10):
            obj_1.run()
            obj_2.walk()
        self.assertNotEqual(obj_1.distance, obj_2.distance)

class TournamentTest(TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(cls):
        cls.runner_1 = Runner_2('Усэйн', 10)
        cls.runner_2 = Runner_2('Андрей', 9)
        cls.runner_3 = Runner_2('Ник',3)

    @classmethod
    def tearDownClass(cls):
        for _, j in cls.all_results.items():
            print(j)

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(cls):
        dict_ = Tournament(90, cls.runner_1, cls.runner_3).start()
        for i, j in dict_.items():
            dict_[i] = j.name
        cls.all_results[str(len(cls.all_results))] = dict_
        cls.assertTrue(cls.all_results[str(len(cls.all_results) - 1)]
              [len(cls.all_results[str(len(cls.all_results) - 1)])] == 'Ник')

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(cls):
        dict_ = Tournament(90, cls.runner_2, cls.runner_3).start()
        for i, j in dict_.items():
            dict_[i] = j.name
        cls.all_results[str(len(cls.all_results))] = dict_
        cls.assertTrue(cls.all_results[str(len(cls.all_results) - 1)]
              [len(cls.all_results[str(len(cls.all_results) - 1)])] == 'Ник')

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(cls):
        dict_ = Tournament(90, cls.runner_1,cls.runner_2, cls.runner_3).start()
        for i, j in dict_.items():
            dict_[i] = j.name
        cls.all_results[str(len(cls.all_results))] = dict_
        cls.assertTrue(cls.all_results[str(len(cls.all_results) - 1)]
              [len(cls.all_results[str(len(cls.all_results) - 1)])] == 'Ник')