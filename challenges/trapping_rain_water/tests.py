
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
    if not hasattr(solution_module, 'trap'):
        return [TestResult("Existence", False, "Function not found")]
    
    func = solution_module.trap

    cases = [
        ([0,1,0,2,1,0,1,3,2,1,2,1], 6, "Standard Case"),
        ([4,2,0,3,2,5], 9, "Deep Valley"),
        ([1,2,3], 0, "Ascending (No Trap)"),
    ]

    for inp, expected, name in cases:
        try:
            start = time.perf_counter()
            res = func(inp[:])
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
    
    def solve_ref(height):
        if not height: return 0
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        ans = 0
        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                ans += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                ans += r_max - height[r]
        return ans

    for i in range(total_random):
        size = random.randint(5, 100)
        height = [random.randint(0, 10) for _ in range(size)]
        
        expected = solve_ref(height)
        
        try:
             res = func(height[:])
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
        
    return results
