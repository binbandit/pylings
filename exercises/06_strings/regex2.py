
# REGEX (CAPTURING GROUPS)
# ========================
#
# What: Parentheses `()` in regex create "groups". 
#       `re.findall` returns a list of all matches.
#
# Why:  To extract specific parts of a pattern (e.g., separating user from domain in email).
#
# How:  r"(\w+)@(\w+)\.com" matches "user@gmail.com" and captures "user" and "gmail".
#       re.findall returns a list of tuples if groups are present.
#
# Task:
# 1. Use `re.findall` to find all emails in the text.
# 2. The regex should capture the username and the domain separately.
#    Input: "Contact alice@example.com or bob@test.org"
#    Output: [('alice', 'example.com'), ('bob', 'test.org')]
#    Note: For simplicity, assume domain can end in anything (use .+, or better \w+\.\w+)

import re

def extract_emails(text):
    # TODO: Write pattern with 2 groups: (\w+)@([\w.]+)
    pattern = r""
    return re.findall(pattern, text)

def test_regex_groups():
    text = "Please email support@pylings.io or admin@google.com for help."
    results = extract_emails(text)
    
    # Needs to capture specific parts, not just the whole email
    # Let's say we want (username, domain)
    
    # We expect results to be list of tuples
    assert ("support", "pylings.io") in results, "Failed to capture groups"
    assert ("admin", "google.com") in results, "Failed to capture second email"
    assert len(results) == 2

if __name__ == "__main__":
    test_regex_groups()
    print("Regex groups passed!")
