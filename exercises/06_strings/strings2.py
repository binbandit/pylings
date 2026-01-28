"""
Concept: F-Strings
F-strings (formatted string literals) allow you to embed expressions inside string literals, using `{}`.

Task: Use an f-string to format the greeting.
"""

def main():
    name = "Python"
    version = 3.12
    
    # FIX ME: Use an f-string to format the message!
    message = "I am learning " + name + " version " + str(version) 
    # That works but isn't an f-string!
    if " f\"" not in open(__file__).read():
        # Ideally we parse code, but simple check:
        # User should write: f"I am learning {name} version {version}"
        raise Exception("Use an f-string!")
    
    print(message)

if __name__ == "__main__":
    main()
