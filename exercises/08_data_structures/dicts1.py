"""
Concept: Dictionaries (Creation)
Dictionaries hold key-value pairs. You create them using curly braces `{key: value}`.

Task: Create a `person` dict with "name": "Alice" and "age": 30.
"""

def main():
    # Create a dictionary representing a person
    # FIX ME: Add "name": "Alice" and "age": 30
    person = {} 
    
    if person.get("name") != "Alice":
        raise Exception("Name is missing or wrong!")
        
    if person.get("age") != 30:
        raise Exception("Age is missing or wrong!")
        
    print("Dictionary created!")

if __name__ == "__main__":
    main()
