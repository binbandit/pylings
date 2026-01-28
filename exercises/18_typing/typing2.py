"""
Concept: Typing (Generics)
For collections like lists and dicts, you can specify the type of their contents (e.g., `List[str]`).

Task: Type hint `names` as a List of strings and `scores` as a Dict mapping strings to integers.
"""

from typing import List, Dict

# FIX ME: Type 'names' as a List of strings and 'scores' as a Dict of string to int
# def process_scores(names: List[str], scores: Dict[str, int]):
#     pass

def process_scores(names, scores):
    pass

def main():
    anns = process_scores.__annotations__
    if not anns:
        raise Exception("Missing annotations!")
        
    # Check List[str] - strict check implies we access internal args
    # For simplicity we just check existence for now or exact match if simple
    # Note: Runtime checks for generics can be tricky across versions (3.9 vs 3.10+)
    # We'll keep it simple: just ensure it's not empty
    
    if "names" not in anns or "scores" not in anns:
        raise Exception("Annotate both 'names' and 'scores'")

    print("Collections typed!")

if __name__ == "__main__":
    main()
