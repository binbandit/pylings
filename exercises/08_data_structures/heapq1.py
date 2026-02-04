"""
Concept: heapq (Priority Queue / Min-Heap)

What:
The `heapq` module implements a min-heap, where the smallest element
is always at index 0. A heap is a binary tree where each parent is
smaller than its children.

Why:
- Efficiently find the smallest (or largest) elements: O(1)
- Add/remove elements in O(log n) - much faster than sorting each time
- Perfect for priority queues (process most urgent task first)
- Used in algorithms like Dijkstra's shortest path, merge k sorted lists

How:
    import heapq

    # Convert list to heap (in-place)
    nums = [5, 1, 8, 3]
    heapq.heapify(nums)         # nums is now a valid heap

    # Get smallest element (without removing)
    smallest = nums[0]          # 1

    # Pop smallest element
    smallest = heapq.heappop(nums)  # Returns 1, removes it

    # Push new element
    heapq.heappush(nums, 2)

    # Get n smallest/largest without modifying
    heapq.nsmallest(3, [5, 1, 8, 3])  # [1, 3, 5]
    heapq.nlargest(2, [5, 1, 8, 3])   # [8, 5]

Task:
Use `heapq.nsmallest()` to find the 3 smallest numbers in `nums`.
Assign the result to `smallest`.
"""

import heapq


def main():
    nums = [10, 2, 5, 1, 9, 3, 7]

    # TODO: Use heapq.nsmallest(n, iterable) to find 3 smallest
    smallest = []

    # Verification
    if smallest == []:
        raise Exception("smallest is empty! Use heapq.nsmallest(3, nums)")

    if smallest != [1, 2, 3]:
        raise Exception(
            f"Expected [1, 2, 3], got {smallest}\nUse heapq.nsmallest(3, nums)"
        )

    print(f"The 3 smallest numbers are: {smallest}")
    print("heapq exercise completed!")


if __name__ == "__main__":
    main()
