
import time
import random
from collections import deque, defaultdict
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
    if not hasattr(solution_module, 'canFinish'):
        return [TestResult("Existence", False, "Function not found")]
    
    func = solution_module.canFinish

    cases = [
        (2, [[1,0]], True, "Linear Dependency"),
        (2, [[1,0],[0,1]], False, "Cycle"),
        (4, [[1,0],[2,0],[3,1],[3,2]], True, "Complex DAG"),
    ]

    for n, pre, expected, name in cases:
        try:
            start = time.perf_counter()
            res = func(n, pre)
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
    
    def solve_ref(n, prerequisites):
        adj = defaultdict(list)
        for dest, src in prerequisites:
            adj[src].append(dest)
            
        visited = [0] * n # 0=unvisited, 1=visiting, 2=visited
        
        def dfs(node):
            if visited[node] == 1: return False # Cycle
            if visited[node] == 2: return True
            
            visited[node] = 1
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
            visited[node] = 2
            return True
            
        for i in range(n):
            if not dfs(i):
                return False
        return True

    for i in range(total_random):
        n = random.randint(5, 50)
        # Create random edges
        edges = []
        num_edges = random.randint(n, n*3)
        
        for _ in range(num_edges):
            u = random.randint(0, n-1)
            v = random.randint(0, n-1)
            if u != v:
                edges.append([u,v])
        
        expected = solve_ref(n, edges)
        
        try:
             res = func(n, edges)
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
