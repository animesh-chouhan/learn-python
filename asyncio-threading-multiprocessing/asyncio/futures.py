# A Future is a special low-level awaitable object that represents 
# an eventual result of an asynchronous operation.
# When a Future object is awaited it means that the coroutine will wait until the Future is resolved in some other place.

import asyncio

async def nested():
    return 42

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())
    print(task.done())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    # Futures
    ret_val = await task
    print(task.done())
    print(ret_val)

asyncio.run(main())