
import time
import random
import itertools
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
    if not hasattr(solution_module, 'permute'):
        return [TestResult("Existence", False, "Function not found")]
    
    func = solution_module.permute

    cases = [
        ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]], "Standard 3 items"),
        ([0,1], [[0,1],[1,0]], "2 items"),
        ([1], [[1]], "1 item")
    ]

    for inp, expected, name in cases:
        try:
            start = time.perf_counter()
            res = func(inp[:]) # copy input
            duration = time.perf_counter() - start
            
            # Order doesn't matter, so sort inner items (if needed, but perms are ordered) 
            # and sort outer list
            # We must expect a list of lists.
            if not isinstance(res, list):
                results.append(TestResult(name, False, "Should return a list", duration))
                continue
                
            # Normalize for comparison: sort result
            res_sorted = sorted([tuple(x) for x in res])
            exp_sorted = sorted([tuple(x) for x in expected])
            
            if res_sorted == exp_sorted:
                results.append(TestResult(name, True, "", duration))
            else:
                results.append(TestResult(name, False, f"Result count {len(res)}, expected {len(expected)}", duration))
        except Exception as e:
             results.append(TestResult(name, False, f"Error: {e}"))

    # Dynamic Tests
    passed_random = 0
    total_random = 30
    
    for i in range(total_random):
        size = random.randint(1, 6) # Keep small as factorial grows fast (6! = 720)
        nums = list(range(size))
        random.shuffle(nums)
        
        # Expected
        expected = list(itertools.permutations(nums))
        exp_sorted = sorted(expected)
        
        try:
             res = func(nums[:])
             res_sorted = sorted([tuple(x) for x in res] if res else [])
             
             if res_sorted == exp_sorted:
                 passed_random += 1
             else:
                 results.append(TestResult(f"Random #{i+1}", False, f"Size {size}. Expected {len(exp_sorted)}, got {len(res_sorted)}"))
        except Exception as e:
            results.append(TestResult(f"Random #{i+1}", False, f"Error: {e}"))
            
    if passed_random == total_random:
        results.append(TestResult("30 Randomized Tests", True, "All passed"))
    else:
        results.append(TestResult("Randomized Tests", False, f"Passed {passed_random}/{total_random}"))
        
    return results
