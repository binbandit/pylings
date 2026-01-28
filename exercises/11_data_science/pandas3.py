"""
Concept: Pandas Filtering
You can filter DataFrames using boolean indexing. `df[df['col'] > val]` returns rows where the condition is true.

Task: Filter the DataFrame to keep only people older than 28.
"""

import pandas as pd

def main():
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35]
    })
    
    # FIX ME: Filter for people older than 28
    # oldies = df[df["age"] > 28]
    oldies = df
    
    if len(oldies) != 2:
        raise Exception(f"Expected 2 people, got {len(oldies)}")
        
    if "Alice" in oldies["name"].values:
        raise Exception("Alice should be filtered out!")

    print("Filtering verified!")

if __name__ == "__main__":
    main()
