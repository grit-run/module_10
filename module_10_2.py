from threading import Thread
from time import sleep

QTY_OF_ENEMY = 100


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy_count = QTY_OF_ENEMY

    def run(self):
        print("{}, на нас напали!".format(self.name))
        for i in range(QTY_OF_ENEMY):
            sleep(1)
            self.enemy_count -= self.power
            print("{} сражается {} дней, осталось {} воинов. ".format(self.name, i, self.enemy_count))
            if self.enemy_count <= 0:
                print("{} победил спустя {} дней.".format(self.name, i))
                break


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")

