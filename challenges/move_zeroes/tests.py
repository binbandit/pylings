
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
    if not hasattr(solution_module, 'move_zeroes'):
        return [TestResult("Existence", False, "Function not found")]
    
    func = solution_module.move_zeroes

    cases = [
        ([0,1,0,3,12], [1,3,12,0,0], "Standard"),
        ([0], [0], "Single Zero"),
    ]

    for inp, expected, name in cases:
        inp_copy = inp[:] # Function modifies in-place
        try:
            start = time.perf_counter()
            func(inp_copy)
            duration = time.perf_counter() - start
            if inp_copy == expected:
                results.append(TestResult(name, True, "", duration))
            else:
                results.append(TestResult(name, False, f"Expected {expected}, got {inp_copy}", duration))
        except Exception as e:
             results.append(TestResult(name, False, f"Error: {e}"))

    # Dynamic Tests
    passed_random = 0
    total_random = 30
    
    for i in range(total_random):
        length = random.randint(5, 50)
        nums = [random.choice([0, random.randint(1,9)]) for _ in range(length)]
        
        expected = [x for x in nums if x != 0]
        expected.extend([0] * (length - len(expected)))
        
        nums_copy = nums[:]
        try:
             func(nums_copy)
             if nums_copy == expected:
                 passed_random += 1
             else:
                 results.append(TestResult(f"Random #{i+1}", False, "Incorrect order"))
        except Exception as e:
            results.append(TestResult(f"Random #{i+1}", False, f"Error: {e}"))
            
    if passed_random == total_random:
        results.append(TestResult("30 Randomized Tests", True, "All passed"))
    else:
        results.append(TestResult("Randomized Tests", False, f"Passed {passed_random}/{total_random}"))
        
    return results
