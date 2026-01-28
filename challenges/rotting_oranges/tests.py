
import time
import random
import copy
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
    if not hasattr(solution_module, 'oranges_rotting'):
        return [TestResult("Existence", False, "Function not found")]
    
    func = solution_module.oranges_rotting

    cases = [
        ([[2,1,1],[1,1,0],[0,1,1]], 4, "Standard"),
        ([[2,1,1],[0,1,1],[1,0,1]], -1, "Impossible (Isolated)"),
        ([[0,2]], 0, "No fresh"),
    ]

    for inp, expected, name in cases:
        try:
            start = time.perf_counter()
            res = func(copy.deepcopy(inp))
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
    
    def solve_ref(grid):
        q = deque()
        fresh = 0
        rows, cols = len(grid), len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0: return 0
        
        minutes = 0
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while q and fresh > 0:
            minutes += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, n c))
        
        return minutes if fresh == 0 else -1

    for i in range(total_random):
        rows = random.randint(3, 10)
        cols = random.randint(3, 10)
        # Random grid
        grid = [[random.choice([0,1,1,2]) for _ in range(cols)] for _ in range(rows)]
        
        expected = solve_ref(copy.deepcopy(grid))
        
        try:
             res = func(copy.deepcopy(grid))
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
