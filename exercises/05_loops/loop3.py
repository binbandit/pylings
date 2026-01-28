"""
Concept: While Loops
`while` loops continue running as long as a condition is true. Be careful of infinite loops!

Task: Increment the `count` variable inside the loop so it eventually terminates.
"""

def main():
    count = 0
    while count < 5:
        print(count)
        # FIX ME: We are stuck in an infinite loop! 
        # missing increment!
        if count == 0: # Safety break for running this broken code
             raise Exception("Infinite loop detected! Increment 'count'!")
        
if __name__ == "__main__":
    main()
