
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
    if not hasattr(solution_module, 'threeSum'):
        return [TestResult("Existence", False, "Function not found")]
    
    func = solution_module.threeSum
    
    def normalize(triplets):
        # Sort internal triplet, then sort list of triplets
        return sorted([tuple(sorted(t)) for t in triplets])

    cases = [
        ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]], "Standard Case"),
        ([0,1,1], [], "No Solution"),
        ([0,0,0], [[0,0,0]], "All Zeros"),
    ]

    for inp, expected, name in cases:
        try:
            start = time.perf_counter()
            res = func(inp[:])
            duration = time.perf_counter() - start
            
            if normalize(res) == normalize(expected):
                results.append(TestResult(name, True, "", duration))
            else:
                results.append(TestResult(name, False, f"Mismatch", duration))
        except Exception as e:
             results.append(TestResult(name, False, f"Error: {e}"))

    # Dynamic Tests
    passed_random = 0
    total_random = 30
    
    def solve_ref(nums):
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res

    for i in range(total_random):
        size = random.randint(10, 50)
        nums = [random.randint(-10, 10) for _ in range(size)]
        
        expected = solve_ref(nums[:])
        
        try:
             res = func(nums[:])
             if normalize(res) == normalize(expected):
                 passed_random += 1
             else:
                 results.append(TestResult(f"Random #{i+1}", False, "Mismatch"))
        except Exception as e:
            results.append(TestResult(f"Random #{i+1}", False, f"Error: {e}"))
            
    if passed_random == total_random:
        results.append(TestResult("30 Randomized Tests", True, "All passed"))
    else:
        results.append(TestResult("Randomized Tests", False, f"Passed {passed_random}/{total_random}"))
        
    return results
