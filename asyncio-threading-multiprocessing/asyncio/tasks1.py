import asyncio

async def foo(text, delay):
    print("started " + text)
    await asyncio.sleep(delay=delay)
    print("finished " + text)

# async def main():
#     print("started")
#     task1 = asyncio.create_task(foo("first"))
#     task2 = asyncio.create_task(foo("second"))  
#     print("finished")

# VS

# async def main():
#     print("started")
#     task1 = asyncio.create_task(foo("first", 2))
#     task2 = asyncio.create_task(foo("second", 1))  
#     print(task1)
#     await task1
#     await task2
#     print("finished")

# VS

async def main():
    print("started")
    await foo("first", 2)
    task2 = asyncio.create_task(foo("second", 1))  

    await task2
    print("finished")

asyncio.run(main())