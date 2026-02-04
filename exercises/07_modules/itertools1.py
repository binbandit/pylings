"""
Concept: Itertools - Efficient Iteration Tools

The `itertools` module provides fast, memory-efficient tools for working with
iterators. It's especially useful for combinatorics (permutations, combinations).

Key functions:
- `permutations(iterable, r)`: All possible orderings of r items
  Order matters: (A, B) is different from (B, A)

- `combinations(iterable, r)`: All possible selections of r items
  Order doesn't matter: (A, B) is the same as (B, A), so only one is included

Example:
    from itertools import permutations, combinations

    letters = "AB"

    list(permutations(letters, 2))
    # [('A', 'B'), ('B', 'A')]  -- 2 results (order matters)

    list(combinations(letters, 2))
    # [('A', 'B')]  -- 1 result (order doesn't matter)

For "ABC" with r=2:
- permutations: 3 * 2 = 6 results (each letter can go first, then 2 choices for second)
- combinations: 3 choose 2 = 3 results (AB, AC, BC)

Task:
Use `permutations` to find all possible ordered pairs (length 2) from "ABC".
Store the result as a list in the variable `perms`.
"""

from itertools import permutations


def main():
    letters = "ABC"

    # TODO: Get all permutations of length 2 from 'letters'
    # Hint: permutations(letters, 2) returns an iterator
    # You need to convert it to a list with list(...)
    perms = []  # TODO: Replace with list(permutations(...))

    # Verification
    expected_count = 6  # 3 * 2 = 6 permutations

    if len(perms) == 0:
        raise AssertionError(
            "perms is empty!\n"
            "Use list(permutations(letters, 2)) to get all 2-letter permutations."
        )

    if len(perms) != expected_count:
        raise AssertionError(
            f"Expected {expected_count} permutations, but got {len(perms)}.\n"
            "For 'ABC' with length 2, there should be 6 permutations."
        )

    # Check that specific permutations exist
    required = [("A", "B"), ("B", "A"), ("A", "C"), ("C", "A"), ("B", "C"), ("C", "B")]
    for perm in required:
        if perm not in perms:
            raise AssertionError(
                f"Missing permutation {perm}.\n"
                "Make sure you're using permutations(letters, 2)"
            )

    print(f"All permutations of 'ABC' with length 2:")
    for p in perms:
        print(f"  {p}")
    print(f"\nTotal: {len(perms)} permutations")
    print("Successfully used itertools.permutations!")


if __name__ == "__main__":
    main()
