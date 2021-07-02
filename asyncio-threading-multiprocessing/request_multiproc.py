import time
import requests
from multiprocessing.pool import Pool

N = 100
URL = "http://httpbin.org/uuid"

def get_uuid(s, i):
    response = s.get(URL)
    print(str(i) + ": " + response.json()["uuid"] + "\n", end="")

def main():
    with requests.Session() as s:
        with Pool() as pool:
            pool.starmap(get_uuid, [(s, i) for i in range(100)])

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(end_time - start_time)