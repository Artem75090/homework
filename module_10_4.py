from threading import Thread
from random import randint
from queue import Queue
from time import sleep


class Guest(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        sleep(randint(1, 6))


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for i in guests:
            free_table = False
            for j in self.tables:
                if j.guest is None:
                    j.guest = i
                    i.start()
                    print(f"{i.name} сел(-а) за стол номер {j.number}")
                    free_table = True
                    break
            if not free_table:
                self.queue.put(i)
                print(f"{i.name} в очереди")

    def discuss_guests(self):
        guest_at_table = False
        for i in self.tables:
            if i.guest is not None:
                guest_at_table = True
                break

        while not self.queue.empty() or guest_at_table:
            guest_at_table = False
            for i in self.tables:
                if i.guest is not None:
                    guest_at_table = True
                    break
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None

                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        next_guest.start()
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")


guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]

tables = [Table(number) for number in range(1, 6)]

cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
