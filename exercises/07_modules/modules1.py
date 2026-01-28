"""
Concept: Modules (Standard Library)
Python comes with "batteries included" - a large standard library of modules you can import.

Task: Import the `datetime` module.
"""

def main():
    # FIX ME: Import the datetime module to use datetime.now()
    # import ???
    
    try:
        now = datetime.datetime.now()
        print(f"The time is {now}")
    except NameError:
        print("datetime is not defined!")
        raise

if __name__ == "__main__":
    main()
