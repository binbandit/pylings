"""
Concept: Lists (Removal)
You can remove items from a list using `.remove(value)` or `pop(index)`.

Task: Remove "paper" from the list using `.remove()`.
"""

def main():
    items = ["rock", "paper", "scissors"]
    
    # FIX ME: Remove "paper" from the list
    # items.???("paper")
    
    if "paper" in items:
        raise Exception("Paper is still in the list!")
        
    print("Items updated!")

if __name__ == "__main__":
    main()
