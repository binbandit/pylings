"""
Concept: Error Handling (Try/Except)
`try/except` blocks allow you to handle exceptions gracefully instead of crashing.

Task: Handle the `ZeroDivisionError` that occurs when dividing by zero.
"""

def main():
    # FIX ME: Handle the ZeroDivisionError
    try:
        val = 10 / 0
    except ZeroDivisionError:
        val = 0
    except Exception as e:
        # We shouldn't get here for this specific error if handled correctly
        raise e
        
    if val != 0:
        raise Exception("Did not handle the error correctly (val should be 0)")
    
    print("ZeroDivisionError handled!")

if __name__ == "__main__":
    main()
