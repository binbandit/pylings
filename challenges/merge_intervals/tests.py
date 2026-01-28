
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
    if not hasattr(solution_module, 'merge'):
        return [TestResult("Existence", False, "Function not found")]
    
    func = solution_module.merge

    cases = [
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]], "Standard Case"),
        ([[1,4],[4,5]], [[1,5]], "Touching"),
        ([[1,4],[2,3]], [[1,4]], "Consumed"),
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
    
    def solve_ref(intervals):
        if not intervals: return []
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

    for i in range(total_random):
        size = random.randint(5, 50)
        ints = []
        for _ in range(size):
            s = random.randint(1, 100)
            e = random.randint(s, s + 20)
            ints.append([s,e])
            
        expected = solve_ref(ints[:]) # ref sorts in place so copy if needed, but here we build fresh
        
        try:
             res = func(ints[:]) # give copy
             if res == expected:
                 passed_random += 1
             else:
                 results.append(TestResult(f"Random #{i+1}", False, f"Expected {len(expected)} intervals, got {len(res)}"))
        except Exception as e:
            results.append(TestResult(f"Random #{i+1}", False, f"Error: {e}"))
            
    if passed_random == total_random:
        results.append(TestResult("30 Randomized Tests", True, "All passed"))
    else:
        results.append(TestResult("Randomized Tests", False, f"Passed {passed_random}/{total_random}"))
        
    return results
