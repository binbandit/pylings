"""
Concept: Data Science (Pandas Series)
A Series is a one-dimensional labeled array. It's like a powerful list or dictionary.

Task: Create a Series from a list and calculate the sum.
"""

import pandas as pd

def main():
    data = [10, 20, 30]
    
    # FIX ME: Create a Pandas Series from the data
    # s = pd.Series(data)
    s = None
    
    if s is None or not isinstance(s, pd.Series):
        raise Exception("Not a Pandas Series!")
        
    if s.iloc[0] != 10:
        raise Exception("First element should be 10!")
        
    # FIX ME: Sum the series
    # total = s.sum()
    total = 0
    
    if total != 60:
         raise Exception(f"Sum should be 60, got {total}")

    print("Pandas Series verified!")

if __name__ == "__main__":
    main()
