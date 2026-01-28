"""
Concept: Asyncio

What:
Asyncio allows writing **concurrent** code using the `async` and `await` keywords.
It is cooperative multitasking: code suspends execution (awaits) while waiting for I/O (like network requests), letting other tasks run.

Why:
Crucial for high-performance network servers and web scrapers. It allows handling thousands of connections without thousands of threads.

How:
1. Define a coroutine with `async def`.
2. Pause execution with `await`.
3. Run the top-level entry point with `asyncio.run()`.

```python
import asyncio

async def main():
    print("Start")
    await asyncio.sleep(1) # Non-blocking sleep
    print("Done")

# To run it:
# asyncio.run(main())
```

Task:
Define an `async def` function named `say_hello`.
Inside it:
1. Print "Hello"
2. Await `asyncio.sleep(0.1)`
3. Print "World"
"""

import asyncio

# FIX ME: Define async def say_hello(): ...
async def say_hello():
    pass # Print "Hello", await asyncio.sleep(0.1), print "World"

def main():
    if not asyncio.iscoroutinefunction(say_hello):
        raise Exception("say_hello must be an 'async def' function")
    
    # Run it
    asyncio.run(say_hello())
    
    # Since we can't easily check internal behavior without mocking, 
    # we just check syntax validity and type.

if __name__ == "__main__":
    main()
