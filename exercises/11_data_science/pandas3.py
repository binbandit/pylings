"""
Concept: Pandas DataFrame Filtering with Boolean Indexing

Boolean indexing lets you filter rows based on conditions. The condition
creates a Series of True/False values, and only rows where the condition
is True are returned.

Key concepts:
- `df[condition]` - Filter rows where condition is True
- `df['col'] > value` - Creates a boolean Series
- Combine conditions with `&` (and), `|` (or), `~` (not)
- Always use parentheses around conditions when combining

Examples:
    # Single condition:
    adults = df[df['age'] >= 18]

    # Multiple conditions (note the parentheses!):
    young_adults = df[(df['age'] >= 18) & (df['age'] < 30)]

    # Using isin for multiple values:
    selected = df[df['status'].isin(['active', 'pending'])]

Common filtering patterns:
    df[df['col'] == value]      # Equal to
    df[df['col'] != value]      # Not equal to
    df[df['col'] > value]       # Greater than
    df[df['col'].isnull()]      # Is missing/NaN
    df[df['col'].str.contains('text')]  # String contains

Task: Filter the DataFrame to keep only people whose age is greater than 28.
      (This should return Bob and Charlie, but not Alice)
"""

import pandas as pd


def main():
    df = pd.DataFrame({"name": ["Alice", "Bob", "Charlie"], "age": [25, 30, 35]})

    print("Original DataFrame:")
    print(df)
    print()

    # TODO: Filter the DataFrame to keep only people older than 28
    # Hint: Use boolean indexing: df[df["age"] > 28]
    older_than_28 = None

    # Verification
    if older_than_28 is None:
        raise Exception(
            "older_than_28 is None!\nUse boolean indexing: df[df['age'] > 28]"
        )

    if not isinstance(older_than_28, pd.DataFrame):
        raise Exception(
            f"older_than_28 should be a DataFrame, got {type(older_than_28).__name__}"
        )

    if len(older_than_28) != 2:
        raise Exception(
            f"Expected 2 people older than 28, got {len(older_than_28)}\n"
            "Bob (30) and Charlie (35) should be included."
        )

    names_in_result = older_than_28["name"].tolist()

    if "Alice" in names_in_result:
        raise Exception(
            "Alice (age 25) should NOT be in the result!\nShe is not older than 28."
        )

    if "Bob" not in names_in_result or "Charlie" not in names_in_result:
        raise Exception(
            f"Bob and Charlie should both be in the result.\nGot: {names_in_result}"
        )

    print("Filtered DataFrame (age > 28):")
    print(older_than_28)
    print()
    print("DataFrame filtering verified!")
    print(f"Average age of filtered group: {older_than_28['age'].mean()}")


if __name__ == "__main__":
    main()
