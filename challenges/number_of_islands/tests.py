
import time
import random
import copy
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
    if not hasattr(solution_module, 'num_islands'):
        return [TestResult("Existence", False, "Function not found")]
    
    func = solution_module.num_islands

    cases = [
        (
            [
              ["1","1","1","1","0"],
              ["1","1","0","1","0"],
              ["1","1","0","0","0"],
              ["0","0","0","0","0"]
            ], 
            1, "One Big Island"
        ),
        (
            [
              ["1","1","0","0","0"],
              ["1","1","0","0","0"],
              ["0","0","1","0","0"],
              ["0","0","0","1","1"]
            ],
            3, "Three Islands"
        ),
        (
            [], 0, "Empty Grid"
        )
    ]

    for inp, expected, name in cases:
        # Deep copy because solution might modify grid in place (sink)
        inp_copy = copy.deepcopy(inp)
        try:
            start = time.perf_counter()
            res = func(inp_copy)
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
    
    # Reference implementation (DFS)
    def solve_ref(grid):
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        count = 0
        visited = set()
        
        def dfs(r, c):
            if r<0 or c<0 or r>=m or c>=n or grid[r][c] == "0" or (r,c) in visited:
                return
            visited.add((r,c))
            dfs(r+1, c) # down
            dfs(r-1, c) # up
            dfs(r, c+1) # right
            dfs(r, c-1) # left
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    count += 1
                    dfs(i, j)
        return count

    for i in range(total_random):
        rows = random.randint(1, 20)
        cols = random.randint(1, 20)
        
        # Generate random grid
        # Bias towards islands by clustering? Or just pure random?
        # Pure random might result in many tiny islands or noise.
        # Let's just do random 0/1.
        grid = [[random.choice(["0", "1"]) for _ in range(cols)] for _ in range(rows)]
        
        expected = solve_ref(grid)
        
        # User function might modify grid, so give copy
        grid_copy = copy.deepcopy(grid)
        
        try:
             res = func(grid_copy)
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
