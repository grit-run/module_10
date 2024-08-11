from datetime import datetime
from time import sleep
from threading import Thread

time_start = datetime.now()


def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(word_count):
            file.write("Какое-то слово № {}".format(i) + '\n')
            sleep(0.5)
            from datetime import datetime
    print("Завершилась запись в файл", file_name)


write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

time_end = datetime.now()
print(time_end - time_start)

time_start2 = datetime.now()
thread1 = Thread(target=write_words, args=(10, "example5.txt"))
thread2 = Thread(target=write_words, args=(30, "example6.txt"))
thread3 = Thread(target=write_words, args=(200, "example7.txt"))
thread4 = Thread(target=write_words, args=(100, "example8.txt"))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

time_end2 = datetime.now()
print(time_end2 - time_start2)
