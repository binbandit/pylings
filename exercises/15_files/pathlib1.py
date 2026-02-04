"""
Concept: Pathlib (Modern File Paths)

The `pathlib` module provides an object-oriented approach to filesystem paths.
It's the modern replacement for `os.path` and handles cross-platform differences
automatically (forward slashes on Mac/Linux, backslashes on Windows).

Creating paths:
```python
from pathlib import Path

# Use the / operator to join path components (works on all platforms!)
p = Path("folder") / "subfolder" / "file.txt"
```

Useful Path methods:
- `p.exists()`     - Returns True if path exists
- `p.is_file()`    - Returns True if path is a file
- `p.is_dir()`     - Returns True if path is a directory
- `p.parent`       - Returns the parent directory
- `p.name`         - Returns the filename (last component)
- `p.suffix`       - Returns the file extension (e.g., '.txt')
- `p.read_text()`  - Read file contents as string
- `p.write_text()` - Write string to file

Task:
1. Create a Path object for "exports/data.txt" using the / operator
2. Check if the path exists and store the result in `exists`
"""

from pathlib import Path


def main():
    # TODO: Create a Path object for "exports/data.txt"
    # Use the / operator: Path("exports") / "data.txt"
    file_path = None

    # TODO: Check if the path exists using the .exists() method
    exists = None

    # Verification
    if file_path is None:
        raise Exception(
            'file_path is None!\nHint: Create a Path with Path("exports") / "data.txt"'
        )

    if not isinstance(file_path, Path):
        raise Exception(
            f"file_path should be a Path object, got {type(file_path).__name__}\n"
            "Hint: Use Path() from pathlib to create path objects"
        )

    # Normalize path separators for cross-platform comparison
    path_str = str(file_path).replace("\\", "/")
    if path_str != "exports/data.txt":
        raise Exception(
            f"Path should be 'exports/data.txt', got '{path_str}'\n"
            'Hint: Use Path("exports") / "data.txt"'
        )

    if exists is None:
        raise Exception(
            "exists is None!\nHint: Use file_path.exists() to check if a path exists"
        )

    if not isinstance(exists, bool):
        raise Exception(
            f"exists should be a boolean, got {type(exists).__name__}\n"
            "Hint: .exists() returns True or False"
        )

    print(f"Path verified! 'exports/data.txt' exists: {exists}")


if __name__ == "__main__":
    main()
