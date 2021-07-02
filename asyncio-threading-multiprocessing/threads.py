# https://youtu.be/ecKWiaHCEKs
import os
import math
import time
from threading import Thread

def calc():
    for i in range(30000000):
        math.sqrt(i)

threads = []

for i in range(os.cpu_count()):
    print(f"registering thread {i}")
    threads.append(Thread(target=calc))

start_time = time.time()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print(end_time - start_time)