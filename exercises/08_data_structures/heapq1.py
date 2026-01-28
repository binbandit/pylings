"""
Concept: Heaps (Priority Queue)

What:
A "Heap" is a specialized tree-based data structure that satisfies the heap property. 
In Python, `heapq` implements a **min-heap**, where the smallest element is always at index 0.

Why:
Heaps are incredibly efficient at finding the smallest (or largest) elements in a collection, 
making them perfect for Priority Queues (processing important tasks first).
- Finding min: O(1)
- Adding/Popping: O(log N) - much faster than resorting a list O(N log N).

How:
```python
import heapq
nums = [5, 1, 8, 3]
heapq.heapify(nums)       # Turn list into a heap in-place
smallest = heapq.heappop(nums) # Returns 1
three_smallest = heapq.nsmallest(3, [5, 1, 8, 3]) # [1, 3, 5]
```

Task:
Use `heapq.nsmallest()` to find the **3 smallest numbers** in the list `nums` 
and assign the result to `smallest`.
"""

import heapq

def main():
    nums = [10, 2, 5, 1, 9, 3, 7]
    
    # FIX ME: Use heapq.nsmallest(3, nums)
    # smallest = ...
    smallest = []
    
    if smallest != [1, 2, 3]:
        raise Exception(f"Expected [1, 2, 3], got {smallest}")

if __name__ == "__main__":
    main()
