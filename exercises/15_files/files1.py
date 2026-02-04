"""
Concept: File I/O with Context Managers

Python's `with` statement (context manager) ensures files are properly closed
after use, even if errors occur. This is the recommended way to handle files.

Writing to a file:
```python
with open("filename.txt", "w") as f:
    f.write("content")
```

Reading from a file:
```python
with open("filename.txt", "r") as f:
    content = f.read()
```

The mode argument:
- "w" = write (overwrites existing content)
- "r" = read (default)
- "a" = append (adds to existing content)

Task:
1. Write "Hello World" to "test_file.txt" using a context manager
2. Read the content back from the file into the `content` variable
"""

from pathlib import Path


def main():
    # Helper: ensure clean state
    p = Path("test_file.txt")
    if p.exists():
        p.unlink()

    # TODO: Write "Hello World" to "test_file.txt" using a context manager
    # Use: with open(..., "w") as f:
    #          f.write(...)

    if not p.exists():
        raise Exception(
            "File was not created!\n"
            'Hint: Use \'with open("test_file.txt", "w") as f:\' to open for writing'
        )

    # TODO: Read the content back from "test_file.txt"
    # Use: with open(..., "r") as f:
    #          content = f.read()
    content = ""

    if content != "Hello World":
        raise Exception(
            f"Expected 'Hello World', got '{content}'\n"
            'Hint: Use \'with open("test_file.txt", "r") as f:\' to open for reading'
        )

    # Cleanup
    p.unlink()
    print("File I/O verified!")


if __name__ == "__main__":
    main()
