
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
    if not hasattr(solution_module, 'findMedianSortedArrays'):
        return [TestResult("Existence", False, "Function not found")]
    
    func = solution_module.findMedianSortedArrays

    cases = [
        ([1,3], [2], 2.0, "Odd Total"),
        ([1,2], [3,4], 2.5, "Even Total"),
        ([], [1], 1.0, "One Empty"),
    ]

    for n1, n2, expected, name in cases:
        try:
            start = time.perf_counter()
            res = func(n1, n2)
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
    
    def solve_ref(n1, n2):
        merged = sorted(n1 + n2)
        l = len(merged)
        if l % 2 == 1:
            return float(merged[l // 2])
        else:
            return (merged[l // 2 - 1] + merged[l // 2]) / 2.0

    for i in range(total_random):
        s1 = random.randint(0, 100)
        s2 = random.randint(0, 100)
        if s1 + s2 == 0: s1 = 1 # Avoid empty
        
        n1 = sorted([random.randint(0, 100) for _ in range(s1)])
        n2 = sorted([random.randint(0, 100) for _ in range(s2)])
        
        expected = solve_ref(n1, n2)
        
        try:
             res = func(n1, n2)
             if abs(res - expected) < 1e-5: # Float compare
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
