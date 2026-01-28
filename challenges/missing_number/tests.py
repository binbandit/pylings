
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
    if not hasattr(solution_module, 'missing_number'):
        return [TestResult("Existence", False, "Function not found")]
    
    func = solution_module.missing_number

    cases = [
        ([3,0,1], 2, "n=3, missing 2"),
        ([0,1], 2, "n=2, missing 2"),
        ([9,6,4,2,3,5,7,0,1], 8, "n=9, missing 8"),
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
        n = random.randint(1, 100)
        full_range = list(range(n + 1))
        missing = random.choice(full_range)
        full_range.remove(missing)
        random.shuffle(full_range)
        
        try:
             res = func(full_range)
             if res == missing:
                 passed_random += 1
             else:
                 results.append(TestResult(f"Random #{i+1}", False, f"Expected {missing}, got {res}"))
        except Exception as e:
            results.append(TestResult(f"Random #{i+1}", False, f"Error: {e}"))
            
    if passed_random == total_random:
        results.append(TestResult("30 Randomized Tests", True, "All passed"))
    else:
        results.append(TestResult("Randomized Tests", False, f"Passed {passed_random}/{total_random}"))
        
    return results
