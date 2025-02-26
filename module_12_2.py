import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        self.participants = sorted(self.participants, key=lambda runner: runner.speed)[::-1]
        while self.participants:
            for participant in self.participants[:]:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.r1 = Runner("Усэйн", speed=10)
        self.r2 = Runner("Андрей", speed=9)
        self.r3 = Runner("Ник", speed=3)
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        self.track = Tournament(90, self.r1, self.r3)
        res = self.track.start()
        TournamentTest.all_results.append(res)
        self.assertTrue(res[max(res.keys())] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        self.track = Tournament(90, self.r2, self.r3)
        res = self.track.start()
        TournamentTest.all_results.append(res)
        self.assertTrue(res[max(res.keys())] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        self.track = Tournament(90, self.r1, self.r2, self.r3)
        res = self.track.start()
        TournamentTest.all_results.append(res)
        self.assertTrue(res[max(res.keys())] == "Ник")

    @classmethod
    def tearDownClass(cls):
        for i in TournamentTest.all_results:
            print(i, end='\n')

