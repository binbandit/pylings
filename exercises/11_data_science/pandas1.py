"""
Concept: Pandas Series - One-Dimensional Labeled Data

A Pandas Series is a one-dimensional labeled array. Think of it as a more
powerful list or a single column from a spreadsheet. Each element has an
index (label) and a value.

Key concepts:
- `pd.Series([1, 2, 3])` - Create a Series from a list
- `s.iloc[0]` - Access element by integer position
- `s.loc['label']` - Access element by label/index
- `s.sum()`, `s.mean()`, `s.max()` - Aggregation methods
- Series automatically aligns data by index in operations

Example:
    import pandas as pd
    temperatures = pd.Series([72, 75, 68], index=['Mon', 'Tue', 'Wed'])
    print(temperatures['Tue'])  # 75
    print(temperatures.mean())  # 71.67

Why Series over lists?
- Built-in aggregation methods (sum, mean, std, etc.)
- Labeled indexing for clearer code
- Handles missing data (NaN) gracefully
- Vectorized operations like NumPy

Task:
    1. Create a Pandas Series from the data list [10, 20, 30]
    2. Calculate the sum of all elements (should be 60)
"""

import pandas as pd


def main():
    data = [10, 20, 30]

    # TODO: Create a Pandas Series from the data list
    # Hint: Use pd.Series(data)
    s = None

    # Verification for Series creation
    if s is None:
        raise Exception("s is None! Create a Series using pd.Series(data)")

    if not isinstance(s, pd.Series):
        raise Exception(
            f"s should be a pandas Series, got {type(s).__name__}\n"
            "Use pd.Series() to create it!"
        )

    if s.iloc[0] != 10:
        raise Exception(
            f"First element should be 10, got {s.iloc[0]}\n"
            "Did you pass the correct data list?"
        )

    # TODO: Calculate the sum of all elements in the Series
    # Hint: Series has a .sum() method
    total = None

    # Verification for sum
    if total is None:
        raise Exception("total is None! Use s.sum() to calculate the sum")

    if total != 60:
        raise Exception(
            f"Sum should be 60, got {total}\nUse the .sum() method on your Series!"
        )

    print("Pandas Series verified!")
    print(f"Series:\n{s}")
    print(f"Sum: {total}")
    print(f"Mean: {s.mean()}")
    print(f"Max: {s.max()}")


if __name__ == "__main__":
    main()
