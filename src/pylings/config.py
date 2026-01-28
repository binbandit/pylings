import tomllib
from pathlib import Path
from typing import List
from .model import Exercise

class Config:
    def __init__(self, exercises: List[Exercise]):
        self.exercises = exercises

    @classmethod
    def load(cls, path: Path = Path("info.toml")) -> "Config":
        if not path.exists():
            raise FileNotFoundError(f"Configuration file not found: {path}")
        
        with open(path, "rb") as f:
            data = tomllib.load(f)
        
        exercises = []
        for ex_data in data.get("exercises", []):
            exercises.append(Exercise(
                name=ex_data["name"],
                path=Path(ex_data["path"]),
                mode=ex_data.get("mode", "run"),
                hint=ex_data.get("hint", "")
            ))
        
        return cls(exercises)
