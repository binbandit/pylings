"""
Concept: Pandas DataFrames
A DataFrame is a 2D labeled data structure (like a table or spreadsheet). You can create one from a dictionary of lists.

Task: Create a DataFrame from the `data` dictionary.
"""

import pandas as pd

def main():
    data = {
        "name": ["Alice", "Bob"],
        "age": [25, 30]
    }
    
    # FIX ME: Create a DataFrame from the dict
    # df = pd.DataFrame(data)
    df = None
    
    if df is None or not isinstance(df, pd.DataFrame):
        raise Exception("Not a DataFrame!")
        
    if "name" not in df.columns or "age" not in df.columns:
        raise Exception("Missing columns!")
        
    print("DataFrame created!")

if __name__ == "__main__":
    main()
