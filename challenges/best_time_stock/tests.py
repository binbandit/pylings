
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
    
    if not hasattr(solution_module, 'max_profit'):
        return [TestResult("Existence", False, "Function 'max_profit' not found")]

    func = solution_module.max_profit

    cases = [
        ([7,1,5,3,6,4], 5, "Basic Case (Buy 1, Sell 6)"),
        ([7,6,4,3,1], 0, "No Profit"),
        ([1, 2], 1, "Two Days"),
        ([2, 4, 1], 2, "Dip in middle"),
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

    # Performance Test
    size = 20000
    # Create a scenario where O(n^2) is worst case: descending order then one spike at end?
    # Actually just a long list.
    # [10000, 9999, ..., 0, 10001] -> Profit = 10001 - 0 = 10001
    prices = list(range(size, 0, -1))
    prices.append(size + 10)
    
    try:
        start = time.perf_counter()
        res = func(prices)
        duration = time.perf_counter() - start
        
        expected_perf = size + 9 # (size+10) - 1
        
        if res == expected_perf:
             if duration < 0.1:
                  results.append(TestResult("Performance (O(n))", True, f"Great speed! {duration:.4f}s", duration))
             else:
                  results.append(TestResult("Performance (O(n))", False, f"Too slow ({duration:.4f}s). Aim for O(n).", duration))
        else:
             results.append(TestResult("Performance (O(n))", False, f"Incorrect result. Expected {expected_perf}, got {res}"))

    except Exception as e:
        results.append(TestResult("Performance (O(n))", False, f"Error: {e}"))

    # --- Dynamic Randomized Tests ---
    import random
    
    passed_random = 0
    total_random = 30
    
    def solve_reference(prices):
        # Reference O(n) implementation to check against
        min_p = float('inf')
        max_p = 0
        for p in prices:
            if p < min_p:
                min_p = p
            elif p - min_p > max_p:
                max_p = p - min_p
        return max_p

    for i in range(total_random):
        length = random.randint(1, 1000)
        prices = [random.randint(0, 10000) for _ in range(length)]
        
        expected = solve_reference(prices)
        
        try:
            res = func(prices)
            if res == expected:
                passed_random += 1
            else:
                 results.append(TestResult(f"Random #{i+1}", False, f"Expected {expected}, got {res}"))
        except Exception as e:
            results.append(TestResult(f"Random #{i+1}", False, f"Error: {e}"))

    if passed_random == total_random:
        results.append(TestResult(f"30 Randomized Tests", True, "All passed"))
    else:
        results.append(TestResult(f"Randomized Tests", False, f"Passed {passed_random}/{total_random}"))

    return results
