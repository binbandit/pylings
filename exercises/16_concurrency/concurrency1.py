"""
Concept: Concurrency (Threading)
Threading allows multiple operations to run concurrently. You create a `Thread`, `.start()` it, and `.join()` it to wait for completion.

Task: Start and join the threads to ensure the counter is incremented correctly.
"""

import threading
import time

shared_counter = 0

def increment():
    global shared_counter
    # FIX ME: Just uncomment the increment. In a real scenario we'd need a lock,
    # but for this simple exercise we just want to spawn threads.
    # shared_counter += 1
    pass

def main():
    threads = []
    for _ in range(10):
        t = threading.Thread(target=increment)
        threads.append(t)
        # FIX ME: Start the thread!
        # t.start()
    
    for t in threads:
        # FIX ME: Join the thread!
        # t.join()
        pass
        
    if shared_counter != 10:
        raise Exception(f"Counter should be 10, got {shared_counter}. Did you start/join threads?")
        
    print("Threading verified!")

if __name__ == "__main__":
    main()
