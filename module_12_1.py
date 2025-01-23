import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_1 = Runner('Ivan')
        for _ in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_1 = Runner('Ivan')
        for _ in range(10):
            runner_1.run()
        self.assertEqual(runner_1.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_1 = Runner('Ivan')
        runner_2 = Runner('Petr')
        for _ in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)



if __name__ == '__main__':
    unittest.main()
