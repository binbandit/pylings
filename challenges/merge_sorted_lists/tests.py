
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
    
    if not hasattr(solution_module, 'merge_two_lists'):
        return [TestResult("Existence", False, "Function 'merge_two_lists' not found")]
        
    ListNode = getattr(solution_module, 'ListNode', None)
    if not ListNode:
        return [TestResult("Structure", False, "Class 'ListNode' not found")]

    func = solution_module.merge_two_lists

    def create_linked_list(arr):
        if not arr: return None
        head = ListNode(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head
        
    def nodes_to_list(node):
        res = []
        curr = node
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

    cases = [
        ([1,2,4], [1,3,4], [1,1,2,3,4,4], "Standard Merge"),
        ([], [], [], "Both Empty"),
        ([], [0], [0], "One Empty"),
    ]

    for list1_arr, list2_arr, expected, name in cases:
        try:
            l1 = create_linked_list(list1_arr)
            l2 = create_linked_list(list2_arr)
            
            start = time.perf_counter()
            new_head = func(l1, l2)
            duration = time.perf_counter() - start
            
            res = nodes_to_list(new_head)
            
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
    
    for i in range(total_random):
        # Generate two random sorted lists
        len1 = random.randint(0, 20)
        len2 = random.randint(0, 20)
        l1_arr = sorted([random.randint(0, 100) for _ in range(len1)])
        l2_arr = sorted([random.randint(0, 100) for _ in range(len2)])
        
        expected = sorted(l1_arr + l2_arr)
        
        try:
            ln1 = create_linked_list(l1_arr)
            ln2 = create_linked_list(l2_arr)
            
            res_head = func(ln1, ln2)
            res_list = nodes_to_list(res_head)
            
            if res_list == expected:
                passed_random += 1
            else:
                 results.append(TestResult(f"Random #{i+1}", False, f"Mismatch in merged list"))
        except Exception as e:
            results.append(TestResult(f"Random #{i+1}", False, f"Error: {e}"))

    if passed_random == total_random:
        results.append(TestResult(f"30 Randomized Tests", True, "All passed"))
    else:
        results.append(TestResult(f"Randomized Tests", False, f"Passed {passed_random}/{total_random}"))
        
    return results
