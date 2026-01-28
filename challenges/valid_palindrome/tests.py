
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
    
    if not hasattr(solution_module, 'is_palindrome'):
        return [TestResult("Existence", False, "Function 'is_palindrome' not found")]

    func = solution_module.is_palindrome

    cases = [
        ("A man, a plan, a canal: Panama", True, "Classic Phrase"),
        ("race a car", False, "Not a palindrome"),
        (" ", True, "Empty string/space"),
        ("0P", False, "Numbers comparison"),
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

    # --- Dynamic Randomized Tests ---
    import random
    import string
    
    passed_random = 0
    total_random = 30
    
    def get_random_string(length):
        return ''.join(random.choices(string.ascii_letters + string.digits + " ,.:@", k=length))
        
    for i in range(total_random):
        is_palindrome_case = random.choice([True, False])
        
        if is_palindrome_case:
            # Generate random half, mirror it
            half = get_random_string(random.randint(5, 20))
            # Clean half to just alphanumeric for mirroring
            clean = "".join(ch.lower() for ch in half if ch.isalnum())
            # We want the input to be messy but palindromic in logic
            # So s = half + reversed(half) (logically)
            # But we need to inject noise that IS ignored (punctuation) at random places
            # This is complex. Simpler: Create clean palindrome, then insert random punctuation.
            
            base = get_random_string(10) # Just random noise
            clean_base = "".join(ch.lower() for ch in base if ch.isalnum())
            pal = clean_base + clean_base[::-1]
            
            # Now insert random non-alphanumeric chars into `pal` to make `inp`
            inp = list(pal)
            for _ in range(5):
                idx = random.randint(0, len(inp))
                inp.insert(idx, random.choice(" ,.:@!"))
            inp = "".join(inp)
            expected = True
        else:
            # Just random noise is likely not palindrome
            inp = get_random_string(random.randint(10, 50))
            # Verify it's not accidentally one
            clean = "".join(ch.lower() for ch in inp if ch.isalnum())
            expected = (clean == clean[::-1])
        
        try:
            res = func(inp)
            if res == expected:
                passed_random += 1
            else:
                 results.append(TestResult(f"Random #{i+1}", False, f"Input '{inp[:10]}...'. Expected {expected}, got {res}"))
        except Exception as e:
            results.append(TestResult(f"Random #{i+1}", False, f"Error: {e}"))

    if passed_random == total_random:
        results.append(TestResult(f"30 Randomized Tests", True, "All passed"))
    else:
        results.append(TestResult(f"Randomized Tests", False, f"Passed {passed_random}/{total_random}"))

    return results
