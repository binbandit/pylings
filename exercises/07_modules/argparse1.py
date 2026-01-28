"""
Concept: Argparse (Command Line Arguments)

What:
`argparse` is the standard library for creating user-friendly command-line interfaces.
It handles parsing arguments like `--help`, `--verbose`, or filenames.

Why:
If you want to build a tool like `git` or `ls`, you need to accept inputs from the terminal.

How:
```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="Your name")
args = parser.parse_args()

print(f"Hello {args.name}")
```

Task:
1. Create an ArgumentParser.
2. Add an argument `--count` that accepts an integer (use `type=int`).
3. Parse the argument list `['--count', '5']` (we simulate command line input here).
"""

import argparse

def main():
    parser = argparse.ArgumentParser()
    
    # FIX ME: Add --count argument with type=int
    # parser.add_argument("--count", type=int)
    
    # Simulating command line args: python script.py --count 5
    fake_args = ['--count', '5']
    
    # FIX ME: Parse fake_args
    # args = parser.parse_args(fake_args)
    args = None
    
    if args is None:
        raise Exception("Please parse the arguments")
        
    try:
        if args.count != 5:
            raise Exception(f"Expected count to be 5, got {args.count}")
    except AttributeError:
        raise Exception("The argument 'count' does not exist provided. Did you name it '--count'?")

if __name__ == "__main__":
    main()
