"""
Concept: Control Flow (If/Else)
`if` statements allow you to execute code based on a condition. `else` provides an alternative path if the condition is false.

Task: Add an `else` block to handle the case where `val` is not "Big".
"""

def main():
    val = 5
    if val > 10:
        print("Big")
    # Missing else!
        print("Small")

if __name__ == "__main__":
    main()
