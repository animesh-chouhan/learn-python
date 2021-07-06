import time
import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

N = 100
URL = "http://httpbin.org/uuid"

def get_uuid(s, i):
    response = s.get(URL)
    print(str(i) + ": " + response.json()["uuid"] + "\n", end="")

# https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures
def main():
    with ThreadPoolExecutor() as executor:
    # with ProcessPoolExecutor() as executor:
        with requests.Session() as s:
            for i in range(N):
                executor.submit(get_uuid, s, i)

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print("Finished in " + str(end_time - start_time))