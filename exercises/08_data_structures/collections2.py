"""
Concept: collections.defaultdict

What:
`defaultdict` is a dictionary that never raises KeyError for missing keys.
When you access a missing key, it automatically creates a default value
using a factory function you provide.

Why:
- Eliminates the need for `if key not in dict:` checks
- Makes grouping operations much cleaner
- Common pattern: building lists of items by category
- Reduces bugs from forgotten initialization

How:
    from collections import defaultdict

    # Default value is an empty list
    groups = defaultdict(list)
    groups["fruits"].append("apple")  # No KeyError! Creates [] first.
    groups["fruits"].append("banana")
    # defaultdict(list, {'fruits': ['apple', 'banana']})

    # Default value is 0 (for counting)
    counts = defaultdict(int)
    counts["a"] += 1  # No KeyError! Creates 0 first.
    counts["a"] += 1
    # defaultdict(int, {'a': 2})

    # Without defaultdict (verbose!):
    groups = {}
    if "fruits" not in groups:
        groups["fruits"] = []
    groups["fruits"].append("apple")

Task:
1. Create a defaultdict of lists named `grouped`
2. Group the words by their first letter
   (e.g., "apple" goes under key "a")
"""

from collections import defaultdict


def main():
    words = ["apple", "banana", "apricot", "cherry", "blueberry"]

    # TODO: Create a defaultdict with list as the default factory
    grouped = None

    # TODO: Loop through words and group by first letter
    # Hint: for word in words:
    #           grouped[word[0]].append(word)

    # Verification
    if grouped is None:
        raise Exception("grouped is None! Create it: defaultdict(list)")

    if not isinstance(grouped, defaultdict):
        raise Exception(
            f"grouped should be a defaultdict, got {type(grouped).__name__}\n"
            "Use: defaultdict(list)"
        )

    if len(grouped) == 0:
        raise Exception(
            "grouped is empty! Loop through words and group them by first letter."
        )

    if set(grouped["a"]) != {"apple", "apricot"}:
        raise Exception(
            f"Expected {{'apple', 'apricot'}} under 'a', got {set(grouped['a'])}\n"
            "Group by first letter: grouped[word[0]].append(word)"
        )

    if set(grouped["b"]) != {"banana", "blueberry"}:
        raise Exception(
            f"Expected {{'banana', 'blueberry'}} under 'b', got {set(grouped['b'])}"
        )

    if grouped["c"] != ["cherry"]:
        raise Exception(f"Expected ['cherry'] under 'c', got {grouped['c']}")

    print(f"Grouped words: {dict(grouped)}")
    print("defaultdict exercise completed!")


if __name__ == "__main__":
    main()
