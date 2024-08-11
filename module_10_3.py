from threading import Thread, Lock
from time import sleep
from random import randint


class Bank(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.balance = 0
        self.lock = Lock()

#    def run(self):
#        def __init__(self):
#            Thread.__init__(self)
#            self.balance = 0
#            self.lock = Lock()

    def deposit(self):
        for i in range(100):
            ran_num = randint(50, 500)
            print("Запрос на 'случайное число': {}".format(ran_num))
            self.balance += ran_num
            print("Пополнение: {}. Баланс: {}".format(ran_num, self.balance))
            sleep(0.5)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self):
        for i in range(100):
            ran_num = randint(50, 500)
            print("Звпрос на 'случайное число': {}".format(ran_num))
            if ran_num <= self.balance:
                self.balance -= ran_num
                print("Баланс: {}".format(self.balance))
                sleep(0.5)
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print("Итоговый баланс: {}".format(bk.balance))
