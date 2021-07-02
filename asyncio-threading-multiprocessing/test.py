# https://www.youtube.com/watch?v=t5Bo1Je9EmE

import asyncio

async def foo(text):
    print(text)
    await asyncio.sleep(2)

async def main():
    print("started")
    await foo("first")
    print("finished")

asyncio.run(main())