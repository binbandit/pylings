
import time
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
    
    if not hasattr(solution_module, 'two_sum'):
        return [TestResult("Existence", False, "Function 'two_sum' not found")]

    func = solution_module.two_sum

    # Test Case 1: Basic
    t1_start = time.perf_counter()
    try:
        res = func([2, 7, 11, 15], 9)
        t1_end = time.perf_counter()
        if set(res) == {0, 1}:
            results.append(TestResult("Basic Test", True, "Correct indices", t1_end - t1_start))
        else:
            results.append(TestResult("Basic Test", False, f"Expected [0, 1], got {res}", t1_end - t1_start))
    except Exception as e:
        results.append(TestResult("Basic Test", False, f"Error: {e}"))

    # Test Case 2: Negative Numbers
    try:
        res = func([-1, -2, -3, -4, -5], -8)
        if set(res) == {2, 4}: # -3 + -5 = -8
             results.append(TestResult("Negative Numbers", True, "Correct indices"))
        else:
             results.append(TestResult("Negative Numbers", False, f"Expected [2, 4], got {res}"))
    except Exception as e:
        results.append(TestResult("Negative Numbers", False, f"Error: {e}"))

    # Test Case 3: Performance (O(n) check)
    # Create a large list where the answer is at the very end
    size = 10000
    large_nums = list(range(size))
    target = size - 1 + size - 2 # Sum of last two elements
    
    t_perf_start = time.perf_counter()
    try:
        res = func(large_nums, target)
        t_perf_end = time.perf_counter()
        duration = t_perf_end - t_perf_start
        
        if set(res) == {size-2, size-1}:
             # Strict timeout check. O(n) should be instant (<0.01s). O(n^2) will be slow (~seconds).
             if duration < 0.1:
                 results.append(TestResult("Performance Test (Large Input)", True, f"Great speed! {duration:.4f}s", duration))
             else:
                 results.append(TestResult("Performance Test (Large Input)", False, f"Too slow ({duration:.4f}s). Aim for O(n) complexity!", duration))
        else:
             results.append(TestResult("Performance Test", False, "Incorrect result on large input"))
    except Exception as e:
        results.append(TestResult("Performance Test", False, f"Error: {e}"))

    return results

    # --- Dynamic Randomized Tests ---
    import random
    
    # 30 Random Tests
    passed_random = 0
    total_random = 30
    
    for i in range(total_random):
        # Generate valid problem: [nums], target
        # Pick 2 distinctive indices
        length = random.randint(2, 50)
        nums = [random.randint(-100, 100) for _ in range(length)]
        
        idx1 = random.randint(0, length - 1)
        idx2 = random.randint(0, length - 1)
        while idx1 == idx2:
            idx2 = random.randint(0, length - 1)
            
        target = nums[idx1] + nums[idx2]
        
        # NOTE: There might be multiple solutions with random numbers, but the problem says "exactly one solution".
        # To strictly enforce exactly one, we'd need to be careful, but for checking user correctness
        # if they return ANY valid pair summing to target, that's usually acceptable in looser variations,
        # OR we ensure strictly unique.
        # Let's relax check: if nums[res[0]] + nums[res[1]] == target, pass.
        
        try:
            res = func(nums, target)
            if not res or len(res) != 2:
                results.append(TestResult(f"Random #{i+1}", False, "Invalid return format"))
                continue
            
            if res[0] == res[1]:
                results.append(TestResult(f"Random #{i+1}", False, "Used same element twice"))
                continue
                
            if nums[res[0]] + nums[res[1]] == target:
                passed_random += 1
            else:
                 results.append(TestResult(f"Random #{i+1}", False, f"Sum {nums[res[0]]} + {nums[res[1]]} != {target}"))
        except Exception as e:
             results.append(TestResult(f"Random #{i+1}", False, f"Error: {e}"))

    if passed_random == total_random:
        results.append(TestResult(f"30 Randomized Tests", True, "All passed"))
    else:
        results.append(TestResult(f"Randomized Tests Summary", False, f"Passed {passed_random}/{total_random}"))

    return results
