
import time
import random
import string
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
    if not hasattr(solution_module, 'exist'):
        return [TestResult("Existence", False, "Function not found")]
    
    func = solution_module.exist

    cases = [
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True, "Zigzag"),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True, "Horizontal"),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", False, "Reuse cell check"),
    ]

    for board, word, expected, name in cases:
        try:
            start = time.perf_counter()
            # Deep copy board as user might modify it for visited tracking
            res = func(copy.deepcopy(board), word)
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
    
    def solve_ref(board, word):
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, i):
            if i == len(word): return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False
            
            tmp = board[r][c]
            board[r][c] = "#"
            res = (dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or 
                   dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
            board[r][c] = tmp
            return res
            
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True
        return False

    for i in range(total_random):
        rows = random.randint(3, 8)
        cols = random.randint(3, 8)
        board = [[random.choice(string.ascii_uppercase) for _ in range(cols)] for _ in range(rows)]
        
        # Determine word: 50% chance construct real word from board path, 50% random word
        if random.random() < 0.5:
             # Walk to build word
             w = []
             r, c = random.randint(0, rows-1), random.randint(0, cols-1)
             seen = set()
             path_len = random.randint(3, 8)
             curr_board = copy.deepcopy(board) # Temp tracking
             
             # Simple random walk to build valid word
             valid_path = []
             stack = [(r,c)]
             seen.add((r,c))
             valid_path.append(board[r][c])
             
             curr_r, curr_c = r, c
             
             for _ in range(path_len-1):
                 dirs = [(1,0),(-1,0),(0,1),(0,-1)]
                 random.shuffle(dirs)
                 moved = False
                 for dr, dc in dirs:
                     nr, nc = curr_r + dr, curr_c + dc
                     if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen:
                         seen.add((nr, nc))
                         valid_path.append(board[nr][nc])
                         curr_r, curr_c = nr, nc
                         moved = True
                         break
                 if not moved: break
             
             word = "".join(valid_path)
             # Even with this construction, verify with solver (since random letters could form other words)
        else:
            word = "".join(random.choices(string.ascii_uppercase, k=random.randint(3, 6)))
            
        expected = solve_ref(copy.deepcopy(board), word)
        
        try:
             res = func(copy.deepcopy(board), word)
             if res == expected:
                 passed_random += 1
             else:
                 results.append(TestResult(f"Random #{i+1}", False, f"Expected {expected}, got {res}. Board: {board}, Word: {word}"))
        except Exception as e:
            results.append(TestResult(f"Random #{i+1}", False, f"Error: {e}"))
            
    if passed_random == total_random:
        results.append(TestResult("30 Randomized Tests", True, "All passed"))
    else:
        results.append(TestResult("Randomized Tests", False, f"Passed {passed_random}/{total_random}"))
        
    return results
