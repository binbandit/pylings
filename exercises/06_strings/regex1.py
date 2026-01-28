
# REGULAR EXPRESSIONS (REGEX)
# ===========================
#
# What: A powerful sequence of characters that specifies a search pattern in text.
#
# Why:  Standard strings methods (find, split) aren't enough for complex patterns
#       like "find all email addresses" or "validate phone numbers".
#
# How:  import re
#       match = re.search(r"pattern", text)
#       Common patterns:
#       \d = digit, \w = word char, \s = space
#       + = one or more, * = zero or more, ? = zero or one
#
# Task:
# 1. Use `re.search` to find a phone number pattern "ddd-ddd-dddd" in the text.
#    Use \d{3} for 3 digits.
# 2. Extract the matched string using `.group()`.

import re

def find_phone(text):
    # TODO: Write a regex to match "123-456-7890" format
    pattern = r"" 
    match = re.search(pattern, text)
    if match:
        return match.group()
    return None

def test_regex():
    text = "Call me at 555-019-2834 tomorrow."
    result = find_phone(text)
    assert result == "555-019-2834", f"Expected check, got {result}"
    
    assert find_phone("No number here") is None

if __name__ == "__main__":
    test_regex()
    print("Regex search passed!")
