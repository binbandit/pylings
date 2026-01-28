"""
Concept: Slicing
You can extract parts of a string (or list) using slicing: `[start:end]`.

Task: Slice the first 3 characters of the alphabet.
"""

def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # FIX ME: Slice the string to get 'abc'
    first_three = alphabet[:]
    
    if first_three != "abc":
        raise Exception(f"Expected 'abc', got '{first_three}'")

if __name__ == "__main__":
    main()
