import time
import asyncio
import requests
import functools
import concurrent.futures

N = 100
URL = "http://httpbin.org/uuid"

# Using https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor
# Executing code in thread or process pool: https://docs.python.org/3/library/asyncio-eventloop.html#id14

def get_uuid(s, i):
    response = s.get(URL)
    print(str(i) + ": " + response.json()["uuid"] + "\n", end="")

# async def main():
#     loop = asyncio.get_running_loop()
#     with requests.Session() as s:
#         for i in range(N):
#             await loop.run_in_executor(None, functools.partial(get_uuid, s, i))

async def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        with requests.Session() as s:
            for i in range(N):
                executor.submit(functools.partial(get_uuid, s, i))

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print("Finished in " + str(end_time - start_time))