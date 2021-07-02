# https://youtu.be/ecKWiaHCEKs
import os
import math
import time
from multiprocessing import Process



def calc():
    for i in range(1, 30000000):
        math.sqrt(i)

processes = []

for i in range(os.cpu_count()):
    print(f"registering process {i}")
    processes.append(Process(target=calc))

start_time = time.time()

for thread in processes:
    thread.start()

for thread in processes:
    thread.join()

end_time = time.time()
print(end_time - start_time)