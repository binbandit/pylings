"""
regex2.py - Regex Capturing Groups

Parentheses () create "capturing groups" that extract parts of a match:

    import re
    pattern = r"(\w+)@(\w+)\.com"
    match = re.search(pattern, "user@gmail.com")
    match.group(0)  # "user@gmail.com" (full match)
    match.group(1)  # "user" (first group)
    match.group(2)  # "gmail" (second group)

re.findall() with groups returns a list of tuples:
    re.findall(r"(\w+)@(\w+)", "a@b c@d")  # [("a", "b"), ("c", "d")]

Your task: Write a pattern with two capturing groups to extract email parts:
- Group 1: the username (before @)
- Group 2: the domain (after @)
"""

import re


def extract_emails(text):
    # TODO: Write a pattern with groups: (username)@(domain)
    # Hint: (\w+) matches word characters, @ is literal, ([\w.]+) matches domain
    pattern = r""

    return re.findall(pattern, text)


def main():
    text = "Contact support@pylings.io or admin@google.com for help."
    results = extract_emails(text)

    if len(results) != 2:
        raise Exception(f"Expected 2 email matches, got {len(results)}")

    if ("support", "pylings.io") not in results:
        raise Exception(f"Expected ('support', 'pylings.io') in results, got {results}")

    if ("admin", "google.com") not in results:
        raise Exception(f"Expected ('admin', 'google.com') in results, got {results}")

    print(f"Found emails: {results}")
    print("Regex capturing groups work!")


if __name__ == "__main__":
    main()
