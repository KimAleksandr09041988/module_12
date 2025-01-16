from test_12_1 import RunnerTest
from tests_12_2 import TournamentTest
from unittest import TestSuite, TextTestRunner, TestLoader

runnerTS = TestSuite()
runnerTS.addTest(TestLoader().loadTestsFromTestCase(RunnerTest))
runnerTS.addTest(TestLoader().loadTestsFromTestCase(TournamentTest))

runner = TextTestRunner(verbosity=2)
runner.run(runnerTS)
