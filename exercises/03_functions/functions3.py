"""
Concept: Functions (Logic)
Functions contain logic that operates on inputs.

Task: use the `num` argument in the range() function instead of the hardcoded 1.
"""

def call_me(num):
    for i in range(1): # FIX ME: This only rings once!
        print("Ring!")

def main():
    # Ideally checking output, but for now we trust the user to fix the logic error.
    call_me(3)

if __name__ == "__main__":
    main()
