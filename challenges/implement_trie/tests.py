
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
    if not hasattr(solution_module, 'Trie'):
        return [TestResult("Existence", False, "Class not found")]
    
    Trie = solution_module.Trie

    # Static Case
    try:
        start = time.perf_counter()
        trie = Trie()
        trie.insert("apple")
        r1 = trie.search("apple")   # True
        r2 = trie.search("app")     # False
        r3 = trie.startsWith("app") # True
        trie.insert("app")
        r4 = trie.search("app")     # True
        
        duration = time.perf_counter() - start
        
        if (r1 and not r2 and r3 and r4):
             results.append(TestResult("Standard Flow", True, "", duration))
        else:
             results.append(TestResult("Standard Flow", False, f"Got: {r1}, {r2}, {r3}, {r4}", duration))

    except Exception as e:
        results.append(TestResult("Standard Flow", False, f"Error: {e}"))

    # Dynamic Tests
    passed_random = 0
    total_random = 30
    
    for i in range(total_random):
        # Build reference
        ref_words = set()
        
        try:
            dut = Trie()
            ops_passed = True
            
            # 1. Insert random words
            num_inserts = random.randint(10, 50)
            words = []
            for _ in range(num_inserts):
                w = "".join(random.choices(string.ascii_lowercase, k=random.randint(1, 8)))
                ref_words.add(w)
                dut.insert(w)
                words.append(w)
                
            # 2. Search positive/negative
            for _ in range(20):
                w = "".join(random.choices(string.ascii_lowercase, k=random.randint(1, 8)))
                exp = w in ref_words
                got = dut.search(w)
                if exp != got:
                    ops_passed = False
                    results.append(TestResult(f"Random #{i+1} Search", False, f"Word '{w}', Exp {exp}, Got {got}"))
                    break
            
            if not ops_passed: continue

            # 3. StartsWith positive/negative
            for _ in range(20):
                p = "".join(random.choices(string.ascii_lowercase, k=random.randint(1, 5)))
                # Naive reference check for prefix
                exp = any(rw.startswith(p) for rw in ref_words)
                got = dut.startsWith(p)
                if exp != got:
                    ops_passed = False
                    results.append(TestResult(f"Random #{i+1} Prefix", False, f"Prefix '{p}', Exp {exp}, Got {got}"))
                    break

            if ops_passed:
                passed_random += 1
                
        except Exception as e:
            results.append(TestResult(f"Random #{i+1}", False, f"Error: {e}"))
            
    if passed_random == total_random:
        results.append(TestResult("30 Randomized Tests", True, "All passed"))
    else:
        results.append(TestResult("Randomized Tests", False, f"Passed {passed_random}/{total_random}"))
        
    return results
