
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
    if not hasattr(solution_module, 'LRUCache'):
        return [TestResult("Existence", False, "Class not found")]
    
    LRUCache = solution_module.LRUCache

    # Static Case
    try:
        start = time.perf_counter()
        lru = LRUCache(2)
        lru.put(1, 1) # cache is {1=1}
        lru.put(2, 2) # cache is {1=1, 2=2}
        v1 = lru.get(1)    # return 1
        lru.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        v2 = lru.get(2)    # returns -1 (not found)
        lru.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        v3 = lru.get(1)    # return -1 (not found)
        v4 = lru.get(3)    # return 3
        v5 = lru.get(4)    # return 4
        
        duration = time.perf_counter() - start
        
        if (v1 == 1 and v2 == -1 and v3 == -1 and v4 == 3 and v5 == 4):
            results.append(TestResult("Standard Flow", True, "", duration))
        else:
            results.append(TestResult("Standard Flow", False, f"Got: {v1}, {v2}, {v3}, {v4}, {v5}", duration))

    except Exception as e:
        results.append(TestResult("Standard Flow", False, f"Error: {e}"))

    # Dynamic Tests
    # We will simulate random operations against a python OrderedDict as reference
    from collections import OrderedDict

    passed_random = 0
    total_random = 30
    
    class RefLRU:
        def __init__(self, capacity):
            self.capacity = capacity
            self.cache = OrderedDict()
            
        def get(self, key):
            if key not in self.cache:
                return -1
            self.cache.move_to_end(key)
            return self.cache[key]
            
        def put(self, key, value):
            if key in self.cache:
                self.cache.move_to_end(key)
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)

    for i in range(total_random):
        capacity = random.randint(1, 20)
        ops_count = random.randint(50, 200)
        
        ref = RefLRU(capacity)
        try:
            dut = LRUCache(capacity)
            
            ops_passed = True
            error_msg = ""
            
            for _ in range(ops_count):
                op = random.choice(["put", "get", "put"]) # bias put slightly more or equal
                key = random.randint(1, 20) # Small key space to force collisions/evictions
                
                if op == "put":
                    val = random.randint(1, 100)
                    ref.put(key, val)
                    dut.put(key, val)
                else:
                    exp = ref.get(key)
                    got = dut.get(key)
                    if exp != got:
                        ops_passed = False
                        error_msg = f"Capacity {capacity}. Op get({key}). Exp {exp}, Got {got}"
                        break
            
            if ops_passed:
                passed_random += 1
            else:
                 results.append(TestResult(f"Random #{i+1}", False, error_msg))
                 
        except Exception as e:
            results.append(TestResult(f"Random #{i+1}", False, f"Error: {e}"))
            
    if passed_random == total_random:
        results.append(TestResult("30 Randomized Tests", True, "All passed"))
    else:
        results.append(TestResult("Randomized Tests", False, f"Passed {passed_random}/{total_random}"))
        
    return results
