import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.counter = 0
        self.lock = threading.Lock()

    def deposit(self):
        while self.counter < 199:
            self.lock.acquire()
            while True:
                top_up = randint(50, 500)
                if self.counter % 2 == 0:
                    self.counter += 1
                    if self.balance < 500:
                        self.balance += top_up
                        print(f'Пополнение: {top_up}, Баланс: {self.balance}')
                break
            sleep(0.001)
            self.lock.release()


    def take(self):
        while self.counter < 199:
            self.lock.acquire()
            while True:
                subtract = randint(50, 500)
                if self.counter % 2 != 0:
                    self.counter += 1
                    print(f'Запрос на {subtract}')
                    if self.balance >= subtract:
                        self.balance -= subtract
                        print(f'Снятие: {subtract}, Баланс: {self.balance}')
                    else:
                        print('Запрос отклонён, недостаточно средств')
                break
            sleep(0.001)
            self.lock.release()
        print(f'Итоговый баланс: {self.balance}')



bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
