"""
Concept: Async/Await Basics

What:
Asyncio enables writing concurrent code using `async` and `await` keywords.
It uses cooperative multitasking: code voluntarily suspends while waiting for I/O,
allowing other tasks to run.

Why:
- Handle thousands of connections without thousands of threads
- Perfect for network servers, web scrapers, and I/O-bound applications
- More efficient than threading for I/O operations

How:
1. Define an async function with `async def`
2. Use `await` to pause and wait for async operations
3. Run the entry point with `asyncio.run()`

```python
import asyncio

async def greet():
    print("Starting...")
    await asyncio.sleep(1)  # Non-blocking pause
    print("Done!")

asyncio.run(greet())  # Run the async function
```

Key points:
- `async def` creates a coroutine function
- `await` can only be used inside `async def` functions
- `asyncio.sleep()` is the async version of `time.sleep()`

Task:
Complete the `fetch_data` function to:
1. Print "Fetching data..."
2. Await `asyncio.sleep(0.1)` to simulate network delay
3. Return the string "Data retrieved!"
"""

import asyncio

# I AM NOT DONE


async def fetch_data():
    """Simulate fetching data from a remote source."""
    # TODO: Print "Fetching data..."

    # TODO: Await asyncio.sleep(0.1) to simulate network delay

    # TODO: Return the string "Data retrieved!"
    return None


async def main():
    # Call the async function
    result = await fetch_data()

    # Verification
    if result != "Data retrieved!":
        raise Exception(
            f"fetch_data() returned {result!r}, expected 'Data retrieved!'\n"
            "Hint: Make sure to return the exact string."
        )

    print(f"Success! Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
