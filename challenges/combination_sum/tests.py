
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
    if not hasattr(solution_module, 'combination_sum'):
        return [TestResult("Existence", False, "Function not found")]
    
    func = solution_module.combination_sum
    
    def normalize(combinations):
        # Sort each combo, then sort the list of combos
        return sorted([tuple(sorted(c)) for c in combinations])

    cases = [
        ([2,3,6,7], 7, [[2,2,3],[7]], "Standard Case"),
        ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]], "Multiple matches"),
        ([2], 1, [], "No match"),
    ]

    for cands, target, expected, name in cases:
        try:
            start = time.perf_counter()
            res = func(cands, target)
            duration = time.perf_counter() - start
            
            if not isinstance(res, list):
                 results.append(TestResult(name, False, "Wait, return a list", duration))
                 continue
                 
            norm_res = normalize(res)
            norm_exp = normalize(expected)
            
            if norm_res == norm_exp:
                results.append(TestResult(name, True, "", duration))
            else:
                results.append(TestResult(name, False, f"Expected {len(norm_exp)}, got {len(norm_res)} combinations", duration))
        except Exception as e:
             results.append(TestResult(name, False, f"Error: {e}"))

    # Dynamic Tests
    passed_random = 0
    total_random = 30
    
    def solve_ref(candidates, target):
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            # Include candidates[i]
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            
            # Skip candidates[i]
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res

    for i in range(total_random):
        # Small inputs to avoid massive output space
        size = random.randint(2, 5)
        candidates = sorted(list(set([random.randint(2, 10) for _ in range(size)])))
        target = random.randint(5, 20)
        
        expected = solve_ref(candidates, target)
        
        try:
             res = func(candidates, target)
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
