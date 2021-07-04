# https://docs.python.org/3/library/asyncio-task.html

# Python coroutines are awaitables and therefore can be awaited from other coroutines.
# IMPORTANT: In this documentation the term “coroutine” can be used for two closely related concepts:
# > a coroutine function: an async def function;
# > a coroutine object: an object returned by calling a coroutine function.

import asyncio

async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main())