
import time
import random
from collections import deque
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
    if not hasattr(solution_module, 'Codec'):
        return [TestResult("Existence", False, "Class Codec not found")]
    
    TreeNode = solution_module.TreeNode
    Codec = solution_module.Codec
    
    # Helper to check tree equality
    def is_same_tree(p, q):
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

    # Helper to build tree
    def build_tree(values):
        if not values: return None
        root = TreeNode(values[0])
        queue = deque([root])
        i = 1
        while queue and i < len(values):
            node = queue.popleft()
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        return root

    try:
        start = time.perf_counter()
        ser = Codec()
        deser = Codec()
        
        # Static Case
        root = build_tree([1,2,3,None,None,4,5])
        data = ser.serialize(root)
        if not isinstance(data, str):
            results.append(TestResult("Return Type", False, "serialize must return str"))
            return results
            
        new_root = deser.deserialize(data)
        
        duration = time.perf_counter() - start
        
        if is_same_tree(root, new_root):
            results.append(TestResult("Standard Case", True, "", duration))
        else:
             results.append(TestResult("Standard Case", False, "Restored tree does not match original", duration))

    except Exception as e:
        results.append(TestResult("Standard Case", False, f"Error: {e}"))

    # Dynamic Tests
    passed_random = 0
    total_random = 30
    
    for i in range(total_random):
        size = random.randint(1, 50)
        vals = [random.randint(0, 100) if random.random() > 0.3 else None for _ in range(size)]
        if not vals: vals = [1]
        if vals[0] is None: vals[0] = 1 # Root must exist
        
        root = build_tree(vals)
        
        try:
             ser = Codec()
             deser = Codec()
             data = ser.serialize(root)
             new_root = deser.deserialize(data)
             
             if is_same_tree(root, new_root):
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
