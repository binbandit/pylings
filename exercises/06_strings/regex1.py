"""
regex1.py - Regular Expressions (Basics)

Regular expressions (regex) are patterns for matching text. Python's `re` module
provides regex support.

Basic patterns:
    \d  - matches any digit (0-9)
    \w  - matches any word character (a-z, A-Z, 0-9, _)
    \s  - matches any whitespace
    .   - matches any character except newline

Quantifiers:
    {3}  - exactly 3 of the preceding
    +    - one or more
    *    - zero or more
    ?    - zero or one

Example:
    import re
    re.search(r"\d{3}", "abc123def")  # Finds "123"

Your task: Write a regex pattern to find phone numbers in "123-456-7890" format.
The pattern should match: 3 digits, hyphen, 3 digits, hyphen, 4 digits.
"""

import re


def find_phone(text):
    # TODO: Write a pattern to match phone numbers like "123-456-7890"
    # Hint: Use \d{3} to match 3 digits
    pattern = r""

    match = re.search(pattern, text)
    if match:
        return match.group()
    return None


def main():
    # Test cases
    result = find_phone("Call me at 555-019-2834 tomorrow.")
    if result != "555-019-2834":
        raise Exception(f"Expected '555-019-2834', got '{result}'")

    result = find_phone("No phone number here")
    if result is not None:
        raise Exception(f"Expected None for text without phone, got '{result}'")

    print("Found phone: 555-019-2834")
    print("Regex basics work!")


if __name__ == "__main__":
    main()
