import threading
from time import sleep


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        enemy = 100
        counter = 0
        print(f'{self.name} на нас напали!')

        while True:
            sleep(1)
            if enemy > 0:
                enemy = enemy - self.power
                counter += 1
                enemy = 0 if enemy < 0 else enemy
                print(f'{self.name}, сражается {counter} день(дня)..., осталось {enemy} воинов. ')
            else:
                break
        print(f'{self.name} одержал победу спустя {counter} дней(дня)! ')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
