
import importlib.util
import time
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import List, Any, Callable

@dataclass
class TestResult:
    name: str
    passed: bool
    message: str = ""
    duration: float = 0.0

class ChallengeRunner:
    def __init__(self, challenge_dir: Path):
        self.challenge_dir = challenge_dir
        self.solution_path = challenge_dir / "solution.py"
        self.input_path = challenge_dir / "input.py"
        self.tests_path = challenge_dir / "tests.py"

    def load_module(self, path: Path, module_name: str):
        if not path.exists():
            return None
        spec = importlib.util.spec_from_file_location(module_name, path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            return module
        return None

    def run(self) -> List[TestResult]:
        if not self.solution_path.exists():
            return [TestResult("Load Solution", False, "solution.py not found")]

        # Load Solution
        try:
            solution_module = self.load_module(self.solution_path, "solution")
        except Exception as e:
            return [TestResult("Load Solution", False, f"Syntax Error: {e}")]

        if not self.tests_path.exists():
             return [TestResult("Load Tests", False, "tests.py not found")]

        # Load Tests
        try:
            tests_module = self.load_module(self.tests_path, "tests_suite")
        except Exception as e:
            return [TestResult("Load Tests", False, f"Error loading tests: {e}")]
        
        results = []
        
        # Check if tests module has a 'run_tests' function
        if hasattr(tests_module, 'run_tests'):
            try:
                # Pass the solution module to the test runner so it can call user functions
                user_results = tests_module.run_tests(solution_module)
                results.extend(user_results)
            except Exception as e:
                 results.append(TestResult("Test Execution", False, f"Crash during tests: {e}"))
        else:
            results.append(TestResult("Test Configuration", False, "tests.py missing 'run_tests(solution)' function"))

        return results

    def run_custom_input(self):
        """Allows user to run their solution against custom input defined in input.py"""
        pass # To be implemented if we want a playground mode
