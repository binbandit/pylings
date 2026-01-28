"""
Concept: Asyncio Gather (Parallel Execution)

What:
Simply `await`-ing functions one by one executes them **sequentially**.
To run independent tasks **concurrently** (at the same time), use `asyncio.gather(*tasks)`.

Why:
If you have 3 API calls that take 1 second each:
- Sequential: 1s + 1s + 1s = 3 seconds total.
- Concurrent (Gather): max(1s, 1s, 1s) = ~1 second total.

How:
```python
import asyncio

async def task1(): ...
async def task2(): ...

async def main():
    # Start both at once and wait for both to finish
    results = await asyncio.gather(task1(), task2())
```

Task:
1. Create 3 concurrent tasks of `slow_method`.
2. Use `asyncio.gather` to run them.
3. Ensure the total time is far less than the sum of individual times.
"""

import asyncio
import time

async def slow_method(n):
    await asyncio.sleep(0.1) # Simulate I/O
    return n * 2

async def main():
    start_time = time.perf_counter()
    
    # FIX ME: Run slow_method(1), slow_method(2), slow_method(3) concurrently using gather
    # results = await asyncio.gather(...)
    results = []
    
    end_time = time.perf_counter()
    duration = end_time - start_time
    
    # If they ran sequentially, it would take 0.3s + overhead. 
    # If concurrent, it should take ~0.1s + overhead.
    
    if len(results) != 3:
        raise Exception("Expected 3 results")
        
    if duration > 0.25:
        # This is a heuristic. 0.1s * 3 = 0.3s. 
        # If it runs in parallel it should comfortably be under 0.2s.
        raise Exception(f"Too slow ({duration:.3f}s)! Did you await them sequentially instead of using gather?")

    print(f"Finished in {duration:.3f}s")

if __name__ == "__main__":
    asyncio.run(main())
