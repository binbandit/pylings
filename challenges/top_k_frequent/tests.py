
import time
import random
from collections import Counter
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
    if not hasattr(solution_module, 'topKFrequent'):
        return [TestResult("Existence", False, "Function not found")]
    
    func = solution_module.topKFrequent

    cases = [
        ([1,1,1,2,2,3], 2, [1,2], "Standard Case"),
        ([1], 1, [1], "Single Case"),
    ]

    for nums, k, expected, name in cases:
        try:
            start = time.perf_counter()
            res = func(nums, k)
            duration = time.perf_counter() - start
            
            # Order doesn't matter
            if sorted(res) == sorted(expected):
                results.append(TestResult(name, True, "", duration))
            else:
                results.append(TestResult(name, False, f"Expected {expected}, got {res}", duration))
        except Exception as e:
             results.append(TestResult(name, False, f"Error: {e}"))

    # Dynamic Tests
    passed_random = 0
    total_random = 30
    
    for i in range(total_random):
        size = random.randint(10, 1000)
        # skew distribution to ensure frequency differences
        nums = []
        for v in range(1, 20):
            freq = random.randint(1, 50)
            nums.extend([v] * freq)
        random.shuffle(nums)
        
        k = random.randint(1, 10)
        
        c = Counter(nums)
        expected = [x[0] for x in c.most_common(k)]
        
        try:
             res = func(nums, k)
             # Sort both for comparison
             if sorted(res) == sorted(expected):
                 passed_random += 1
             else:
                 # Handling ties in frequency is tricky. 
                 # If frequencies are equal, any answer is accepted usually, but here we used exact standard counter.
                 # Let's verify frequencies of result match frequencies of expected.
                 res_freqs = sorted([c[x] for x in res], reverse=True)
                 exp_freqs = sorted([c[x] for x in expected], reverse=True)
                 
                 if res_freqs == exp_freqs:
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
