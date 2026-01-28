"""
Concept: Enumerate and Zip

What:
- `enumerate(iterable)`: Takes a list and returns pairs of (index, item).
- `zip(list1, list2)`: Takes multiple lists and pairs their elements together (index 0 with 0, 1 with 1...).

Why:
- Use `enumerate` when you need both the item AND its position (index) in the list.
- Use `zip` when you need to iterate over two related lists at the same time.

How:
```python
# Enumerate
names = ["Alice", "Bob"]
for i, name in enumerate(names):
    print(i, name) # Prints: 0 Alice, 1 Bob

# Zip
ages = [25, 30]
for name, age in zip(names, ages):
    print(name, age) # Prints: Alice 25, Bob 30
```

Task:
1. Use `enumerate` to iterate over `names`.
2. Use `zip` to pair `names` and `ages` together.
"""

def main():
    names = ["Alice", "Bob", "Charlie"]
    ages = [24, 50, 18]
    
    # FIX ME: Use enumerate to print 0: Alice, 1: Bob, etc.
    # for i, name in enumerate(names):
    #     print(f"{i}: {name}")
    
    # FIX ME: Use zip to print Alice is 24, etc.
    # for name, age in zip(names, ages):
    #     print(f"{name} is {age}")
    
    # To pass this test, we'll collect the results
    result_enum = []
    # for i, name in enumerate(names):
    #     result_enum.append((i, name))
        
    result_zip = []
    # for name, age in zip(names, ages):
    #     result_zip.append((name, age))

    if result_enum != [(0, "Alice"), (1, "Bob"), (2, "Charlie")]:
        raise Exception("Enumerate logic missing or incorrect")
        
    if result_zip != [("Alice", 24), ("Bob", 50), ("Charlie", 18)]:
        raise Exception("Zip logic missing or incorrect")

if __name__ == "__main__":
    main()
