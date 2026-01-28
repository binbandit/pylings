"""
Concept: String Concatenation
You can combine strings using the `+` operator.

Task: Combine `hello` and `world` with a space in between.
"""

def main():
    part1 = "Hello"
    part2 = "World"
    
    # FIX ME: Concatenate part1 and part2 with a space in between!
    result = part1 + part2
    
    if result != "Hello World":
        raise Exception(f"Expected 'Hello World', got '{result}'")

if __name__ == "__main__":
    main()
