"""
Concept: Match Case (Python 3.10+)
`match` statements are a powerful way to branch logic based on the structure and value of data. It's similar to `switch` in other languages but more powerful.

Task: Add a `case 418:` block to handle the "I'm a teapot" status code.
"""

def main():
    status = 418
    
    match status:
        case 200:
            print("OK")
        case 404:
            print("Not Found")
        case 500:
            print("Internal Server Error")
        # FIX ME: Add a case for 418 that prints "I'm a teapot"
        case _:
            print("Unknown status")
            raise Exception("We need to handle the teapot!")

if __name__ == "__main__":
    main()
