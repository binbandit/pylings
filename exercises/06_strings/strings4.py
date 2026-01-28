"""
Concept: String Methods
Strings have built-in methods like `.upper()`, `.lower()`, `.strip()`.

Task: Convert the string to lowercase using `.lower()`.
"""

def main():
    msg = "STOP SHOUTING!"
    
    # FIX ME: Make the message lowercase!
    quiet_msg = msg
    
    if quiet_msg != "stop shouting!":
        raise Exception("Still too loud!")

if __name__ == "__main__":
    main()
