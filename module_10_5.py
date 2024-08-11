from datetime import datetime

filenames = ["./file {number}.txt".format(number=number) for number in range(1, 5)]
print(filenames)


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        row = file.readline()
        while row:
            all_data.append(row)
            row = file.readline()

start = datetime.now()

for filename in filenames:
    read_info(filename)

end = datetime.now()
print(end - start)
