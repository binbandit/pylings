
import time
import random
from typing import List, Any
from dataclasses import dataclass

@dataclass
class TestResult:
    name: str
    passed: bool
    message: str = ""
    duration: float = 0.0

def run_tests(solution_module) -> List[TestResult]:
    results = []
    if not hasattr(solution_module, 'search'):
        return [TestResult("Existence", False, "Function 'search' not found")]
    
    func = solution_module.search

    # Static Cases
    cases = [
        ([-1,0,3,5,9,12], 9, 4, "Found (Standard)"),
        ([-1,0,3,5,9,12], 2, -1, "Not Found"),
        ([5], 5, 0, "Single Element Found"),
        ([5], 0, -1, "Single Element Not Found"),
    ]

    for nums, target, expected, name in cases:
        try:
            start = time.perf_counter()
            res = func(nums, target)
            duration = time.perf_counter() - start
            if res == expected:
                results.append(TestResult(name, True, "", duration))
            else:
                results.append(TestResult(name, False, f"Expected {expected}, got {res}", duration))
        except Exception as e:
             results.append(TestResult(name, False, f"Error: {e}"))

    # Dynamic Randomized Tests (30)
    passed_random = 0
    total_random = 30
    
    for i in range(total_random):
        size = random.randint(10, 1000)
        nums = sorted([random.randint(-5000, 5000) for _ in range(size)])
        
        # 50% chance target exists
        if random.choice([True, False]):
            target = random.choice(nums)
            # Find expected index (binary search or built-in)
            # built-in index() finds FIRST occurrence, which is correct for standard binary search usually,
            # but standard binary search might land on ANY occurrence if duplicates exist.
            # Problem statement usually implies unique or 'any valid index'. 
            # Leetcode 704 usually consists of unique integers. We'll ensure unqiue.
            nums = sorted(list(set(nums))) # Dedup and sort
            target = random.choice(nums)
            expected = nums.index(target)
        else:
            target = random.randint(-6000, 6000)
            while target in nums: # Ensure it doesn't exist
                target = random.randint(-6000, 6000)
            expected = -1
            
        try:
            res = func(nums, target)
            if res == expected:
                passed_random += 1
            else:
                 results.append(TestResult(f"Random #{i+1}", False, f"Expected {expected}, got {res}"))
        except Exception as e:
            results.append(TestResult(f"Random #{i+1}", False, f"Error: {e}"))

    if passed_random == total_random:
        results.append(TestResult("30 Randomized Tests", True, "All passed"))
    else:
        results.append(TestResult("Randomized Tests", False, f"Passed {passed_random}/{total_random}"))

    # Performance Test (O(log n) vs O(n))
    # Search in massive array
    size_huge = 5_000_000
    huge_nums = list(range(size_huge)) # 0 to 4999999
    target_huge = size_huge - 1
    
    start = time.perf_counter()
    res = func(huge_nums, target_huge)
    duration = time.perf_counter() - start
    
    if res == target_huge:
        # Binary search on 5M items should be extremely fast (log2(5M) ~= 22 steps) -> instant
        # Linear search would take noticeable time in Python (e.g. 0.2s - 0.5s)
        if duration < 0.05: 
             results.append(TestResult("Performance O(log n)", True, f"Great speed! {duration:.5f}s", duration))
        else:
             results.append(TestResult("Performance O(log n)", False, f"Too slow ({duration:.4f}s). Is it O(n)?", duration))
    else:
         results.append(TestResult("Performance Test", False, "Incorrect result"))

    return results
