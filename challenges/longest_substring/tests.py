
import time
import random
import string
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
    if not hasattr(solution_module, 'length_of_longest_substring'):
        return [TestResult("Existence", False, "Function not found")]
    
    func = solution_module.length_of_longest_substring

    cases = [
        ("abcabcbb", 3, "Basic (abc)"),
        ("bbbbb", 1, "Repeating (b)"),
        ("pwwkew", 3, "Subsequence vs Substring (wke)"),
        ("", 0, "Empty"),
        (" ", 1, "Space"),
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
    
    def solve_ref(s):
        seen = {}
        max_len = 0
        start = 0
        for i, char in enumerate(s):
            if char in seen and seen[char] >= start:
                start = seen[char] + 1
            seen[char] = i
            max_len = max(max_len, i - start + 1)
        return max_len

    for i in range(total_random):
        length = random.randint(5, 50)
        # Use smaller charset to ensure repeats happen
        inp = "".join(random.choices("abcdef", k=length))
        expected = solve_ref(inp)
        
        try:
             res = func(inp)
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
