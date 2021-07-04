# https://www.youtube.com/watch?v=t5Bo1Je9EmE

import asyncio

async def foo(text, delay):
    print("started " + text)
    await asyncio.sleep(delay=delay)
    print("finished " + text)

# NOTE: asyncio.sleep() blocks for delay seconds but suspends the current task,
# allowing other tasks to run. See: https://docs.python.org/3/library/asyncio-task.html

# async def main():
#     print("started")
#     await foo("first", 2)
#     await foo("second", 1)
#     print("finished")

# The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.
async def main():
    print("started")
    task1 = asyncio.create_task(foo("first", 2))
    task2 = asyncio.create_task(foo("second", 1))
    await task1
    await task2
    print("finished")

asyncio.run(main())