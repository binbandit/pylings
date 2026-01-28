"""
Concept: Control Flow (Elif)
`elif` (else if) allows you to check multiple conditions sequentially.

Task: Add an `elif` block to check if `val` is a medium number (between 10 and 100).
"""

def main():
    val = 50
    if val < 10:
        print("Small")
    # Fix me: Add an elif to check if val is between 10 and 100!
    # elif ???:
    #     print("Medium")
    else:
        print("Large")
        if val == 50:
             raise Exception("Should be caught by elif!")

if __name__ == "__main__":
    main()
