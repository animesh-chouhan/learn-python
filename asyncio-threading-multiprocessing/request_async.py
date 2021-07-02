import asyncio
import time
import requests

N = 100
URL = "http://httpbin.org/uuid"

async def get_uuid(s, i):
    response = s.get(URL)
    print(str(i) + ": " + response.json()["uuid"])

async def main():
    tasks = []
    with requests.Session() as s:
        for i in range(N):
            tasks.append(asyncio.create_task(get_uuid(s, i)))

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(end_time - start_time)