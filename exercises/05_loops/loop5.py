"""
Concept: Continue
The `continue` statement skips the rest of the current iteration and jumps to the next one.

Task: Use `continue` to skip even numbers.
"""

def main():
    sum_vals = 0
    for i in range(10):
        if i % 2 == 0:
            # FIX ME: Skip even numbers!
            pass
        
        sum_vals += i
    
    if sum_vals != 25: # Sum of 1, 3, 5, 7, 9 is 25
         raise Exception(f"Sum should be 25, got {sum_vals}. Did you skip evens?")

if __name__ == "__main__":
    main()
