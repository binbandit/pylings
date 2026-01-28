"""
Concept: File I/O (Context Managers)
The `with` statement (context manager) ensures that files are properly closed after use, even if errors occur.

Task: Write "Hello World" to "test_file.txt" and then read it back.
"""

from pathlib import Path

def main():
    # Helper: ensure clean state
    p = Path("test_file.txt")
    if p.exists(): p.unlink()
    
    # FIX ME: Write "Hello World" to "test_file.txt" using a context manager
    # with open("test_file.txt", "w") as f:
    #     f.write("Hello World")
    
    if not p.exists():
        raise Exception("File was not created!")
        
    # FIX ME: Read the content back
    # with open("test_file.txt", "r") as f:
    #     content = f.read()
    content = ""
    
    if content != "Hello World":
        raise Exception(f"Expected 'Hello World', got '{content}'")
        
    # Cleanup
    p.unlink()
    print("File I/O verified!")

if __name__ == "__main__":
    main()
