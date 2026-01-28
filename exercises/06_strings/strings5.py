"""
Concept: Split and Join
`.split()` breaks a string into a list. `.join()` combines a list into a string.

Task: Split the CSV string and then join it into a pipe-separated string.
"""

def main():
    shopping_list = "apple,banana,orange"
    
    # FIX ME: Split the string into a list of items!
    items = []
    
    if items != ["apple", "banana", "orange"]:
        raise Exception("Expected a list of fruits!")
    
    # FIX ME: Join them back with a pipe separator!
    pipe_list = ""
    
    if pipe_list != "apple|banana|orange":
         raise Exception("Expected pipe separated string!")

if __name__ == "__main__":
    main()
