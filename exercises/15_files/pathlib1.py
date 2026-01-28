"""
Concept: Pathlib (Modern File Paths)

What:
The `pathlib` module offers classes representing filesystem paths with semantics appropriate for different operating systems.
It effectively replaces `os.path` with an object-oriented approach.

Why:
- It handles `/` vs `\` automatically across Windows/Mac/Linux.
- Methods like `.exists()`, `.read_text()`, `.parent` are much cleaner than nested `os.path` calls.
- You can join paths using the `/` operator!

How:
```python
from pathlib import Path

# Create a path object
p = Path("folder") / "subfolder" / "file.txt"

# Check existence
if p.exists():
    content = p.read_text()

# Get parent directory
parent = p.parent
```

Task:
1. Create a Path object for the file "data.txt" inside a folder "exports".
2. Assign this path to the variable `file_path`.
3. Check if it exists and assign the boolean result to `exists`.
"""

from pathlib import Path

def main():
    # FIX ME: Create the path object "exports/data.txt" using the / operator
    # file_path = Path("exports") / "data.txt"
    file_path = None
    
    # FIX ME: Check if it exists
    # exists = file_path.exists()
    exists = None
    
    if not isinstance(file_path, Path):
        raise Exception("file_path should be a Path object")
        
    # We check the string representation to ensure cross-platform compatibility isn't the issue
    # but the structure is correct.
    if str(file_path).replace("\\", "/") != "exports/data.txt":
         raise Exception("Path structure is incorrect. Did you use 'exports' / 'data.txt'?")
         
    if exists is None:
        raise Exception("Please check for existence")

if __name__ == "__main__":
    main()
