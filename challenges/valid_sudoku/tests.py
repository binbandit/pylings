
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
    if not hasattr(solution_module, 'is_valid_sudoku'):
        return [TestResult("Existence", False, "Function not found")]
    
    func = solution_module.is_valid_sudoku

    base_valid = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    
    # Create invalid case by duplicating '5' in first row
    invalid1 = copy.deepcopy(base_valid)
    invalid1[0][2] = "5"

    cases = [
        (base_valid, True, "Standard Valid"),
        (invalid1, False, "Invalid Row"),
    ]

    for inp, expected, name in cases:
        try:
            start = time.perf_counter()
            res = func(inp)
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
    
    def solve_ref(board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rows[r]: return False
                if val in cols[c]: return False
                
                idx = (r // 3) * 3 + (c // 3)
                if val in boxes[idx]: return False
                
                rows[r].add(val)
                cols[c].add(val)
                boxes[idx].add(val)
        return True

    for i in range(total_random):
        # Generate random board: 
        # Start empty, fill random cells with random digits 1-9
        board = [["."]*9 for _ in range(9)]
        
        # Fill some cells
        num_fills = random.randint(10, 40)
        for _ in range(num_fills):
            r, c = random.randint(0,8), random.randint(0,8)
            board[r][c] = str(random.randint(1,9))
            
        expected = solve_ref(board)
        
        try:
             # Deep copy just in case
             res = func(copy.deepcopy(board))
             if res == expected:
                 passed_random += 1
             else:
                 results.append(TestResult(f"Random #{i+1}", False, f"Expected {expected}, got {res}. Board partial: {board[0]}..."))
        except Exception as e:
            results.append(TestResult(f"Random #{i+1}", False, f"Error: {e}"))
            
    if passed_random == total_random:
        results.append(TestResult("30 Randomized Tests", True, "All passed"))
    else:
        results.append(TestResult("Randomized Tests", False, f"Passed {passed_random}/{total_random}"))
        
    return results
