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
    time_end = datetime.now()
    print(time_end - time_start)


thread1 = Thread(target=write_words, args=(10, "example1.txt"))
thread2 = Thread(target=write_words, args=(30, "example2.txt"))
thread3 = Thread(target=write_words, args=(200, "example3.txt"))
thread4 = Thread(target=write_words, args=(100, "example4.txt"))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
