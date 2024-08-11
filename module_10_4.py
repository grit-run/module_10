import queue
from random import randint
from threading import Thread
from time import sleep

guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe():
    def __init__(self, *number):
        self.queue = queue.Queue()
        self.tables = number

    def guest_arrival(self, *guests):
        for guest in guests:
            if any(True for i in self.tables if i.guest is None):
                table = [i for i in self.tables if i.guest is None][0]
                print("{} сел(-а) за стол номер {}".format(guest.name, table.number))
                table.guest = guest
                guest.start()
            else:
                self.queue.put(guest)
                print("{} в очереди".format(guest.name))

    def discuss_guests(self):
        while not self.queue.empty() or any(False for i in self.tables if i.guest):
            for table in (i for i in self.tables if i.guest):
                if table.guest.is_alive():
                    table.guest.join()
                    print("{} покушал(-а) и ушел(ушла)".format(table.guest.name))
                    print("Стол номер {} свободен".format(table.number))
                    table.guest = None
                if not self.queue.empty():
                    table.guest = self.queue.get()
                    print("{} вышел(-ла) из очереди сел(-а) за стол номер {}".format(table.guest.name, table.number))
                    table.guest.start()


tables = [Table(number) for number in range(1, 6)]

guests = [Guest(name) for name in guests_names]

cafe = Cafe(*tables)

cafe.guest_arrival(*guests)

cafe.discuss_guests()

