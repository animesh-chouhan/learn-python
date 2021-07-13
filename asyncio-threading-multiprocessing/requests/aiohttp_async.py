from asyncio.tasks import gather
import time
import asyncio
import aiohttp

N = 100
URL = "http://httpbin.org/uuid"

# NOTE: This won't work because requests doesn't support await and is blocking i.e requests.get() isn't awaitable
# https://stackoverflow.com/questions/33357233/when-to-use-and-when-not-to-use-python-3-5-await/33399896#33399896
# async def get_uuid(s, i):
#     response = await s.get(URL)
#     # response = s.get(URL)
#     print(str(i) + ": " + response.json()["uuid"])

# async def main():
#     tasks = []
#     with requests.Session() as s:
#         for i in range(N):
#             tasks.append(asyncio.create_task(get_uuid(s, i)))
#     await asyncio.gather(*tasks)

# https://www.youtube.com/watch?v=bs9tlDFWWdQ
# Read this: https://docs.aiohttp.org/en/stable/http_request_lifecycle.html#aiohttp-request-lifecycle


async def get_uuid(s, i):
    # Read why "async with": https://stackoverflow.com/questions/55234194/why-do-i-have-to-use-async-with-when-using-the-aiohttp-module
    async with s.get(URL) as response:
        data = await response.json()
        print(str(i) + ": " + response.json()["uuid"] + "\n", end="")


async def main():
    tasks = []
    async with aiohttp.ClientSession() as s:
        for i in range(N):
            tasks.append(asyncio.create_task(get_uuid(s, i)))
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print("Finished in ", end_time - start_time)
