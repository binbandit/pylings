
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
    
    if not hasattr(solution_module, 'climb_stairs'):
        return [TestResult("Existence", False, "Function 'climb_stairs' not found")]

    func = solution_module.climb_stairs

    # F(n) = F(n-1) + F(n-2)
    # 0, 1, 2, 3, 5, 8, 13, 21...
    # wait: 
    # n=1: 1 way (1)
    # n=2: 2 ways (1+1, 2)
    # n=3: 3 ways (1+1+1, 1+2, 2+1)
    # n=4: 5 ways
    
    cases = [
        (2, 2, "2 Steps"),
        (3, 3, "3 Steps"),
        (5, 8, "5 Steps"), 
    ]

    for inp, expected, name in cases:
        try:
            start = time.perf_counter()
            res = func(inp)
            duration = time.perf_counter() - start
            
            if res == expected:
                results.append(TestResult(f"Case: {name}", True, "", duration))
            else:
                results.append(TestResult(f"Case: {name}", False, f"Expected {expected}, got {res}", duration))
        except Exception as e:
             results.append(TestResult(f"Case: {name}", False, f"Error: {e}"))

    # Performance / Recursion Check
    # If using naive recursion O(2^n), n=35 will take seconds.
    # If using DP O(n), it will be instant.
    large_n = 35
    # Fib(35) approx 9 million, actually let's calculate exact: 14930352
    expected_35 = 14930352 
    
    try:
        start = time.perf_counter()
        res = func(large_n)
        duration = time.perf_counter() - start
        
        if res == expected_35:
             if duration < 0.1:
                  results.append(TestResult("DP Check (n=35)", True, f"Instant! {duration:.4f}s", duration))
             else:
                  results.append(TestResult("DP Check (n=35)", False, f"Too slow ({duration:.4f}s). Use Memoization or Iteration!", duration))
        else:
             results.append(TestResult("DP Check (n=35)", False, f"Result incorrect.", duration))
    except Exception as e:
        results.append(TestResult("DP Check (n=35)", False, f"Error: {e}", 0.0))

    # --- Dynamic Randomized Tests ---
    import random
    
    passed_random = 0
    total_random = 30
    
    # Simple reference implementation to check correctness (iterative)
    def solve_reference(n):
        if n <= 2: return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
    
    for i in range(total_random):
        n = random.randint(1, 40) # Keep n small enough for reference to be fast, but covered by logic
        expected = solve_reference(n)
        
        try:
            res = func(n)
            if res == expected:
                passed_random += 1
            else:
                 results.append(TestResult(f"Random #{i+1}", False, f"n={n}. Expected {expected}, got {res}"))
        except Exception as e:
            results.append(TestResult(f"Random #{i+1}", False, f"Error: {e}"))

    if passed_random == total_random:
        results.append(TestResult(f"30 Randomized Tests", True, "All passed"))
    else:
        results.append(TestResult(f"Randomized Tests", False, f"Passed {passed_random}/{total_random}"))

    return results
