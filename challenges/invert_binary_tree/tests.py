
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
    
    if not hasattr(solution_module, 'invert_tree'):
        return [TestResult("Existence", False, "Function 'invert_tree' not found")]
        
    TreeNode = getattr(solution_module, 'TreeNode', None)
    if not TreeNode:
        return [TestResult("Structure", False, "Class 'TreeNode' not found")]

    func = solution_module.invert_tree

    # Tree helpers (BFS for array conversion)
    def create_tree(arr):
        if not arr: return None
        # Leetcode style array to tree: [4,2,7,1,3,6,9]
        # Not strictly necessary to implement full level order parser if we hardcode test cases manually
        # But let's build a simple one.
        nodes = [TreeNode(val) if val is not None else None for val in arr]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    # Simple equality check
    def is_same_tree(p, q):
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

    # Let's construct trees manually for simplicity
    
    # Case 1: [2, 1, 3] -> [2, 3, 1]
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    expected = TreeNode(2, TreeNode(3), TreeNode(1))
    
    try:
        start = time.perf_counter()
        new_root = func(root)
        duration = time.perf_counter() - start
        
        if is_same_tree(new_root, expected):
            results.append(TestResult("Simple Tree", True, "", duration))
        else:
            results.append(TestResult("Simple Tree", False, "Tree structure incorrect", duration))
    except Exception as e:
        results.append(TestResult("Simple Tree", False, f"Error: {e}"))

    # --- Dynamic Randomized Tests ---
    import random
    
    passed_random = 0
    total_random = 30
    
    def invert_tree_ref(node):
        if not node: return None
        new_node = TreeNode(node.val)
        new_node.left = invert_tree_ref(node.right)
        new_node.right = invert_tree_ref(node.left)
        return new_node

    for i in range(total_random):
        # Generate random tree array (level order-ish)
        size = random.randint(1, 20)
        arr = [random.randint(0, 100) for _ in range(size)]
        # Add some Nones to make it interesting
        # Not easily perfectly applicable with the `create_tree` helper above which is basic
        # Let's just use full dense trees or simple arrays for now to prevent formation issues
        
        root = create_tree(arr)
        expected_root = invert_tree_ref(root)
        
        # We need to recreate the input root because `func` might modify it in place!
        # The reference implementation created a new tree, but user might not.
        # Actually, let's create two identical trees.
        root_input = create_tree(arr)
        
        try:
            res_root = func(root_input)
            if is_same_tree(res_root, expected_root):
                passed_random += 1
            else:
                 results.append(TestResult(f"Random #{i+1}", False, "Tree structure mismatch"))
        except Exception as e:
            results.append(TestResult(f"Random #{i+1}", False, f"Error: {e}"))

    if passed_random == total_random:
        results.append(TestResult(f"30 Randomized Tests", True, "All passed"))
    else:
        results.append(TestResult(f"Randomized Tests", False, f"Passed {passed_random}/{total_random}"))

    return results
