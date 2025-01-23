import unittest
import module_12_1
import module_12_2

runner_test = unittest.TestSuite()
runner_test.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
runner_test.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runner_test)