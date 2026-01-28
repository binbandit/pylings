from dataclasses import dataclass
from pathlib import Path
from typing import Literal

@dataclass
class Exercise:
    name: str
    path: Path
    mode: Literal["run", "test"] = "run"
    hint: str = ""

    def __str__(self):
        return self.name
