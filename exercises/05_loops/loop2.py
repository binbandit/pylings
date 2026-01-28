"""
Concept: Range
`range(n)` generates a sequence of numbers from 0 up to (but not including) n. It is commonly used with loops.

Task: Use `range(10)` to loop 10 times.
"""

def main():
    # Print the numbers 0 to 9 using range()
    for i in range(1): # FIX ME: This only prints 0. Make it print up to 9!
        print(i)
        if i == 9:
            return
            
    raise Exception("Did not check all numbers!")

if __name__ == "__main__":
    main()
