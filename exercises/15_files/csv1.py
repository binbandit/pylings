"""
Concept: CSV (Comma-Separated Values)

CSV is a simple text format where each line is a record and values are
separated by commas. It's widely used for data exchange between applications.

Why it matters:
- Excel, Google Sheets, and databases can export/import CSV
- Simple format that's easy to read and debug
- Python's `csv` module handles edge cases (quotes, commas in values, etc.)

Reading CSV:
```python
import csv

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # Each row is a list: ['value1', 'value2', ...]
```

Writing CSV:
```python
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age'])  # Header
    writer.writerow(['Alice', 30])    # Data row
```

Note: We use `io.StringIO` here to simulate a file in memory.

Task:
Read all rows from the CSV reader into a list called `rows`.
"""

import csv
import io


def main():
    # We use io.StringIO to simulate a file in memory (no disk I/O needed)
    csv_content = "Name,Score\nAlice,100\nBob,85"
    f = io.StringIO(csv_content)

    # Create a CSV reader from the file-like object
    reader = csv.reader(f)

    # TODO: Read all rows from the reader into a list
    # Hint: You can convert an iterator to a list using list()
    rows = []

    # Verification: Should get header + 2 data rows = 3 rows total
    if len(rows) != 3:
        raise Exception(
            f"Expected 3 rows, got {len(rows)}\n"
            "Hint: Use list(reader) to read all rows at once"
        )

    if rows[0] != ["Name", "Score"]:
        raise Exception(
            f"First row should be the header ['Name', 'Score'], got {rows[0]}"
        )

    if rows[1][0] != "Alice":
        raise Exception(f"First data row should start with 'Alice', got {rows[1][0]}")

    if rows[2][1] != "85":
        raise Exception(
            f"Bob's score should be '85', got {rows[2][1]}\n"
            "Note: CSV values are always strings!"
        )

    print("CSV parsing verified!")


if __name__ == "__main__":
    main()
