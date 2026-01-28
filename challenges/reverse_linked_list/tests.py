
import time
from typing import List, Any, Optional
from dataclasses import dataclass

@dataclass
class TestResult:
    name: str
    passed: bool
    message: str = ""
    duration: float = 0.0

# Helpers to handle ListNode
def list_to_nodes(lst):
    if not lst: return None
    # Assuming ListNode is dynamically loaded from solution_module
    # We will get the class from the module passed in
    return None # Placeholder, we need the class.

def nodes_to_list(node):
    res = []
    curr = node
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res

def run_tests(solution_module) -> List[TestResult]:
    results = []
    
    if not hasattr(solution_module, 'reverse_list'):
        return [TestResult("Existence", False, "Function 'reverse_list' not found")]
        
    ListNode = getattr(solution_module, 'ListNode', None)
    if not ListNode:
        return [TestResult("Structure", False, "Class 'ListNode' not found")]

    func = solution_module.reverse_list

    # Re-implement helper now that we have ListNode class
    def create_linked_list(arr):
        if not arr: return None
        head = ListNode(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head

    cases = [
        ([1,2,3,4,5], [5,4,3,2,1], "1->5"),
        ([1,2], [2,1], "1->2"),
        ([], [], "Empty"),
    ]

    for inp_list, expected_list, name in cases:
        try:
            head = create_linked_list(inp_list)
            
            start = time.perf_counter()
            new_head = func(head)
            duration = time.perf_counter() - start
            
            res_list = nodes_to_list(new_head)
            
            if res_list == expected_list:
                results.append(TestResult(f"Case: {name}", True, "", duration))
            else:
                results.append(TestResult(f"Case: {name}", False, f"Expected {expected_list}, got {res_list}", duration))
        except Exception as e:
             results.append(TestResult(f"Case: {name}", False, f"Error: {e}"))

    # --- Dynamic Randomized Tests ---
    import random
    
    passed_random = 0
    total_random = 30
    
    for i in range(total_random):
        # Generate random list
        length = random.randint(0, 50)
        inp_list = [random.randint(0, 100) for _ in range(length)]
        expected_list = inp_list[::-1]
        
        try:
            head = create_linked_list(inp_list)
            new_head = func(head)
            res_list = nodes_to_list(new_head)
            
            if res_list == expected_list:
                passed_random += 1
            else:
                 results.append(TestResult(f"Random #{i+1}", False, f"Expected {expected_list[:5]}..., got {res_list[:5]}..."))
        except Exception as e:
            results.append(TestResult(f"Random #{i+1}", False, f"Error: {e}"))

    if passed_random == total_random:
        results.append(TestResult(f"30 Randomized Tests", True, "All passed"))
    else:
        results.append(TestResult(f"Randomized Tests", False, f"Passed {passed_random}/{total_random}"))

    return results
