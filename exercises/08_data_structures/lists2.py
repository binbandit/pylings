"""
Concept: Lists (Methods)
Lists have methods like `.append()` to add items to the end.

Task: Append the number 6 to the `numbers` list.
"""

def main():
    numbers = [1, 2, 3, 4, 5]
    
    # FIX ME: Append the number 6 to the list
    # ???
    
    if len(numbers) != 6 or numbers[-1] != 6:
        raise Exception("Did not append 6!")
        
    print("List appended!")

if __name__ == "__main__":
    main()
