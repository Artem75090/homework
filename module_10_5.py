from multiprocessing import Pool
from time import time


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())


list_files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt', ]

start_time = time()

for i in list_files:
    read_info(i)

res_time = time() - start_time
print(res_time)

# start_time = time()
#
# if __name__ == '__main__':
#     with Pool(4) as p:
#         p.map(read_info, list_files)
#
# res_time = time() - start_time
# print(res_time)
