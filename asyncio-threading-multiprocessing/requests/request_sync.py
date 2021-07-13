import time
import requests

N = 100
URL = "http://httpbin.org/uuid"


def get_uuid(s, i):
    response = s.get(URL)
    print(str(i) + ": " + response.json()["uuid"] + "\n", end="")


def main():
    with requests.Session() as s:
        for i in range(N):
            get_uuid(s, i)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print("Finished in ", end_time - start_time)
