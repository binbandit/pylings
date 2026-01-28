"""
Concept: Break
The `break` statement exits a loop immediately.

Task: Use `break` to stop the loop when `x` equals 5.
"""

def main():
    for i in range(10):
        print(i)
        if i == 5:
            # FIX ME: Stop the loop when i is 5!
            pass 
        
        if i > 5:
            raise Exception("Should have broken at 5!")

if __name__ == "__main__":
    main()
