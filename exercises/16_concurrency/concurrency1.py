"""
Concept: Threading (Concurrent Execution)

What:
Threading allows multiple operations to run concurrently within the same process.
Each thread can execute independently, making it useful for I/O-bound tasks.

Why:
- Handle multiple operations simultaneously (e.g., downloading files while updating UI)
- Improve responsiveness in applications
- Utilize waiting time during I/O operations

How:
1. Create a Thread object with a target function: `t = threading.Thread(target=my_func)`
2. Start the thread: `t.start()` - begins execution in the background
3. Join the thread: `t.join()` - wait for the thread to complete

```python
import threading

def worker():
    print("Working...")

t = threading.Thread(target=worker)
t.start()   # Begin execution
t.join()    # Wait for completion
```

Important: Without `.join()`, the main program might exit before threads finish!

Task:
1. Start each thread using the `.start()` method
2. Join each thread using the `.join()` method to wait for completion
3. The counter should reach 10 after all threads finish
"""

import threading

counter = 0
lock = threading.Lock()


def increment():
    """Increment the shared counter safely using a lock."""
    global counter
    with lock:
        counter += 1


def main():
    global counter
    counter = 0

    threads = []
    for _ in range(10):
        t = threading.Thread(target=increment)
        threads.append(t)
        # TODO: Start the thread using t.start()
        pass

    for t in threads:
        # TODO: Join the thread using t.join() to wait for it to complete
        pass

    # Verification
    if counter != 10:
        raise Exception(
            f"Counter is {counter}, expected 10.\n"
            "Hint: Did you start() and join() all the threads?"
        )

    print("All threads completed successfully!")
    print(f"Final counter value: {counter}")


if __name__ == "__main__":
    main()
