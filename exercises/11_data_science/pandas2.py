"""
Concept: Pandas DataFrames - Two-Dimensional Labeled Data

A DataFrame is a 2D labeled data structure - like a spreadsheet or SQL table.
It's the most commonly used Pandas object. Each column is a Series, and columns
can have different data types.

Key concepts:
- `pd.DataFrame(dict)` - Create from a dictionary of lists
- `df['column']` - Access a column (returns a Series)
- `df.columns` - List of column names
- `df.shape` - (rows, columns) tuple
- `df.head()` - First 5 rows
- `df.describe()` - Statistical summary

Creating DataFrames:
    # From dictionary (column-oriented):
    df = pd.DataFrame({
        'name': ['Alice', 'Bob'],
        'age': [25, 30]
    })

    # From list of dicts (row-oriented):
    df = pd.DataFrame([
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30}
    ])

Task: Create a DataFrame from the provided dictionary containing names and ages.
"""

import pandas as pd


def main():
    # Data to convert into a DataFrame
    data = {"name": ["Alice", "Bob"], "age": [25, 30]}

    # TODO: Create a DataFrame from the data dictionary
    # Hint: Use pd.DataFrame(data)
    df = None

    # Verification for DataFrame creation
    if df is None:
        raise Exception("df is None! Create a DataFrame using pd.DataFrame(data)")

    if not isinstance(df, pd.DataFrame):
        raise Exception(
            f"df should be a pandas DataFrame, got {type(df).__name__}\n"
            "Use pd.DataFrame() to create it!"
        )

    # Check columns exist
    if "name" not in df.columns:
        raise Exception(
            f"DataFrame is missing 'name' column.\nColumns found: {list(df.columns)}"
        )

    if "age" not in df.columns:
        raise Exception(
            f"DataFrame is missing 'age' column.\nColumns found: {list(df.columns)}"
        )

    # Check data is correct
    if len(df) != 2:
        raise Exception(f"DataFrame should have 2 rows, got {len(df)}")

    if df["name"].iloc[0] != "Alice":
        raise Exception(f"First name should be 'Alice', got '{df['name'].iloc[0]}'")

    print("DataFrame created successfully!")
    print(f"\nDataFrame:\n{df}")
    print(f"\nShape: {df.shape} (rows, columns)")
    print(f"Columns: {list(df.columns)}")
    print(f"Average age: {df['age'].mean()}")


if __name__ == "__main__":
    main()
