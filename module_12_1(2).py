import logging
import unittest
import tests_12_4


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner_1 = tests_12_4.Runner('Ivan', speed=-10)
            for _ in range(10):
                runner_1.walk()
            self.assertEqual(runner_1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            runner_1 = tests_12_4.Runner(125)
            for _ in range(10):
                runner_1.run()
            self.assertEqual(runner_1.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")

    # def test_challenge(self):
    #     runner_1 = tests_12_4.Runner('Ivan')
    #     runner_2 = tests_12_4.Runner('Petr')
    #     for _ in range(10):
    #         runner_1.run()
    #         runner_2.walk()
    #     self.assertNotEqual(runner_1.distance, runner_2.distance)
