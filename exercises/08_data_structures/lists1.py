"""
Concept: Lists (Creation)
Lists are ordered, mutable collections of items. You create them using square brackets `[]`.

Task: Create a list named `fruits` containing "apple", "banana", and "cherry".
"""

def main():
    # Create a list of fruits with "apple", "banana", "cherry"
    fruits = [] # FIX ME: Fill the list!
    
    if len(fruits) != 3:
        raise Exception("List is empty or wrong length!")
        
    if fruits[1] != "banana":
        raise Exception("Second fruit should be banana!")
        
    print("Fruit list created successfully!")

if __name__ == "__main__":
    main()
