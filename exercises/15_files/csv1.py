"""
Concept: CSV (Comma Separated Values)

What:
CSV is a common text data format where values are separated by commas.
Python's `csv` module reads and writes these files easily.

Why:
Data exchange! Excel, databases, and APIs often export to CSV. You will likely need to parse one.

How:
```python
import csv

# Writing
with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', 30])

# Reading
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row) # ['Name', 'Age'] ...
```

Task:
1. Initialize the `csv_file` variable with specific data.
2. Use `csv.reader` to parse the simulated file content.
"""

import csv
import io

def main():
    # We use io.StringIO to simulate a file for this exercise so we don't write to disk
    csv_content = "Name,Score\nAlice,100\nBob,85"
    f = io.StringIO(csv_content)
    
    reader = csv.reader(f)
    
    # FIX ME: Read the rows from reader into a list
    # rows = list(reader)
    rows = []
    
    # Should get header + 2 data rows = 3 rows total
    if len(rows) != 3:
        raise Exception(f"Expected 3 rows, got {len(rows)}")
        
    if rows[1][0] != "Alice":
        raise Exception("First data row should be Alice")

if __name__ == "__main__":
    main()
