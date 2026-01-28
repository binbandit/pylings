"""
Concept: List Slicing
You can extract a sub-list using slicing `[start:end]`. 

Task: Extract the middle three elements [20, 30, 40] using slicing.
"""

def main():
    numbers = [10, 20, 30, 40, 50]
    
    # FIX ME: Use slicing to get [20, 30, 40]
    middle = [] 
    
    if middle != [20, 30, 40]:
        raise Exception(f"Expected [20, 30, 40], got {middle}")

if __name__ == "__main__":
    main()
