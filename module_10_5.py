import multiprocessing
from datetime import datetime

filenames = ["./file {number}.txt".format(number=number) for number in range(1, 5)]


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while file.readline():
            all_data.append(file.readline())


#start = datetime.now()
#
#for filename in filenames:
#    read_info(filename)
#
#end = datetime.now()
#print(end - start)

if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        start1 = datetime.now()
        pool.map(read_info, filenames)

    end1 = datetime.now()
    print(end1 - start1)

# Линейный вызов 0:00:01.767815

# Многопроцессный 0:00:00.611422
