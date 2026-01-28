import subprocess
import sys
from dataclasses import dataclass
from typing import Tuple
from .model import Exercise

@dataclass
class CheckResult:
    success: bool
    output: str
    error: str

class Checker:
    @staticmethod
    def run_exercise(exercise: Exercise) -> CheckResult:
        try:
            result = subprocess.run(
                [sys.executable, str(exercise.path)],
                capture_output=True,
                text=True,
                timeout=5
            )
            success = result.returncode == 0
            return CheckResult(success, result.stdout, result.stderr)
        except subprocess.TimeoutExpired:
            return CheckResult(False, "", "Execution timed out")
        except Exception as e:
            return CheckResult(False, "", str(e))
