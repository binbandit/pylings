"""
Concept: asyncio.gather (Running Tasks Concurrently)

What:
By default, awaiting coroutines one-by-one runs them sequentially.
`asyncio.gather()` runs multiple coroutines concurrently and waits for all to complete.

Why:
Sequential vs Concurrent execution time comparison:
- Sequential: 3 tasks x 1 second each = 3 seconds total
- Concurrent: 3 tasks running together = ~1 second total (the slowest task)

This is crucial for performance when making multiple independent I/O calls!

How:
```python
import asyncio

async def task_a():
    await asyncio.sleep(1)
    return "A"

async def task_b():
    await asyncio.sleep(1)
    return "B"

async def main():
    # Run both tasks concurrently
    results = await asyncio.gather(task_a(), task_b())
    print(results)  # ['A', 'B']

asyncio.run(main())
```

The `gather()` function:
- Takes multiple coroutines as arguments
- Runs them all concurrently
- Returns a list of results in the same order as the input

Task:
Use `asyncio.gather()` to run three `fetch_user()` calls concurrently.
The tasks should complete in ~0.1 seconds, not ~0.3 seconds!
"""

import asyncio
import time

# I AM NOT DONE


async def fetch_user(user_id: int) -> dict:
    """Simulate fetching a user from a database."""
    await asyncio.sleep(0.1)  # Simulate network delay
    return {"id": user_id, "name": f"User_{user_id}"}


async def main():
    start = time.perf_counter()

    # TODO: Use asyncio.gather() to fetch users 1, 2, and 3 concurrently
    # Replace the empty list with: await asyncio.gather(fetch_user(1), fetch_user(2), fetch_user(3))
    results = []

    elapsed = time.perf_counter() - start

    # Verification
    if len(results) != 3:
        raise Exception(
            f"Expected 3 results, got {len(results)}.\n"
            "Hint: Use asyncio.gather() with three fetch_user() calls."
        )

    if elapsed > 0.25:
        raise Exception(
            f"Took {elapsed:.2f}s - too slow!\n"
            "Hint: Are you using asyncio.gather() to run tasks concurrently?\n"
            "Sequential execution would take ~0.3s, concurrent should be ~0.1s."
        )

    print(f"Fetched {len(results)} users in {elapsed:.2f}s")
    for user in results:
        print(f"  - {user}")


if __name__ == "__main__":
    asyncio.run(main())
