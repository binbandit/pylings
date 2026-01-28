
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
    if not hasattr(solution_module, 'contains_duplicate'):
        return [TestResult("Existence", False, "Function not found")]
    
    func = solution_module.contains_duplicate

    cases = [
        ([1,2,3,1], True, "Found Duplicate"),
        ([1,2,3,4], False, "All Distinct"),
    ]

    for inp, expected, name in cases:
        try:
            start = time.perf_counter()
            res = func(inp)
            duration = time.perf_counter() - start
            if res == expected:
                results.append(TestResult(name, True, "", duration))
            else:
                results.append(TestResult(name, False, f"Expected {expected}, got {res}", duration))
        except Exception as e:
             results.append(TestResult(name, False, f"Error: {e}"))

    # Dynamic Tests
    passed_random = 0
    total_random = 30
    
    for i in range(total_random):
        size = random.randint(10, 100)
        nums = [random.randint(0, 1000) for _ in range(size)]
        
        has_dupe = len(nums) != len(set(nums))
        
        # Force duplicate cases roughly 50%
        if random.choice([True, False]) and not has_dupe:
            nums.append(nums[0])
            has_dupe = True
            
        try:
             res = func(nums)
             if res == has_dupe:
                 passed_random += 1
             else:
                 results.append(TestResult(f"Random #{i+1}", False, f"Expected {has_dupe}, got {res}"))
        except Exception as e:
            results.append(TestResult(f"Random #{i+1}", False, f"Error: {e}"))
            
    if passed_random == total_random:
        results.append(TestResult("30 Randomized Tests", True, "All passed"))
    else:
        results.append(TestResult("Randomized Tests", False, f"Passed {passed_random}/{total_random}"))
        
    return results
