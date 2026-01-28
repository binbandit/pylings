
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
    
    if not hasattr(solution_module, 'is_valid'):
        return [TestResult("Existence", False, "Function 'is_valid' not found")]

    func = solution_module.is_valid

    cases = [
        ("()", True, "Simple ()"),
        ("()[]{}", True, "Multiple types"),
        ("(]", False, "Mismatch"),
        ("([)]", False, "Nested wrong"),
        ("{[]}", True, "Nested correct"),
        ("]", False, "Single close"),
        ("", True, "Empty string"),
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
    
    passed_random = 0
    total_random = 30
    
    def generate_valid_parentheses(n):
        # Generate a valid string of length 2*n
        if n == 0: return ""
        # Simple strategy: () + valid(n-1), or (valid(k)) + valid(m)
        # For simplicity, let's just do nested or adjacent basic structures
        # or use a proper generator. 
        # Simpler: build a string by inserting pair at random position? No.
        # Strategy: Maintain a balanced count.
        s = []
        def generate(p, left, right, parens="()"):
            if right >= n:
                s.append("".join(p))
                return
            if left < n:
                generate(p + [parens[0]], left + 1, right, parens)
            if right < left:
                generate(p + [parens[1]], left, right + 1, parens)
                
        # That generates ALL combinations, too slow.
        # We just want ONE random one.
        
        res = []
        stack = [] # keep track of open brackets
        pairs = {')':'(', ']':'[', '}':'{'}
        opens = ['(', '[', '{']
        closes = {v:k for k,v in pairs.items()}
        
        # Determine sequence of operations: n opens, n closes.
        # Must never have closes > opens.
        ops = ([1]*n) + ([-1]*n) 
        random.shuffle(ops) 
        
        # This shuffle doesn't guarantee validity (might close too early).
        # Better: Walk and choose open/close randomly if valid.
        
        balance = 0
        current_opens = [] # stack of types
        
        # Let's try constructing a valid string by recursive insertion
        # String S -> () | [] | {} | (S) | [S] | {S} | SS
        
        # Heuristic approach for this exercise:
        # 50% chance generate valid, 50% chance generate invalid noise
        pass

    # Simplified Generator
    def get_case():
        is_valid_case = random.choice([True, False])
        if is_valid_case:
            # Construct a valid one
            # Start with "()" and repeatedly insert "[]", "{}", "()" at random positions
            s = "()"
            for _ in range(random.randint(5, 15)):
                pair = random.choice(["()", "[]", "{}"])
                idx = random.randint(0, len(s))
                s = s[:idx] + pair + s[idx:]
            return s, True
        else:
            # Construct invalid
            # Start valid then mess it up
            s = "()"
            for _ in range(random.randint(5, 15)):
                pair = random.choice(["()", "[]", "{}"])
                idx = random.randint(0, len(s))
                s = s[:idx] + pair + s[idx:]
            
            # Corrupt it: Remove a char, or flip one
            if len(s) > 0:
                idx = random.randint(0, len(s)-1)
                s = s[:idx] + s[idx+1:] # Remove char -> odd length -> invalid
            return s, False

    for i in range(total_random):
        inp, expected = get_case()
        try:
            res = func(inp)
            if res == expected:
                passed_random += 1
            else:
                # Need to be careful: accidentally generating a valid string when trying to make invalid is hard
                # But removing 1 char from a valid string of parens ALWAYS makes it invalid (odd length or mismatch)
                # UNLESS it was empty.
                results.append(TestResult(f"Random #{i+1}", False, f"Input len {len(inp)}. Expected {expected}, got {res}"))
        except Exception as e:
            results.append(TestResult(f"Random #{i+1}", False, f"Error: {e}"))

    if passed_random >= total_random * 0.9: # Allow small margin of error in generator logic? No, strict.
        if passed_random == total_random:
             results.append(TestResult(f"30 Randomized Tests", True, "All passed"))
        else:
             results.append(TestResult(f"Randomized Tests", False, f"Passed {passed_random}/{total_random}"))
    else:
        results.append(TestResult(f"Randomized Tests", False, f"Failed many. Passed {passed_random}/{total_random}"))

    return results
