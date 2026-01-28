"""
Concept: Script vs Module logic
The `if __name__ == "__main__":` block ensures that code only runs when the file is executed directly, not when it's imported as a module.

Task: Wrap the print statement in the `if __name__ == "__main__":` block.
"""

# FIX ME: This print statement is running even when importing!
# It should only run when the script is executed directly.
print("I am running global code!")

def main():
    print("I am main!")

if __name__ == "__main__":
    main()
