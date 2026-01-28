"""
Concept: Importing from Modules
You can import specific functions or classes from a module using `from ... import ...`.

Task: Import the `say_hello` function from the `my_lib` module (which is in the same directory).
"""

def main():
    # FIX ME: Import say_hello from my_lib
    # from my_lib import say_hello
    
    try:
        msg = say_hello()
        if msg != "Hello from my_lib!":
            raise Exception("Wrong message!")
        print(msg)
    except NameError:
        print("say_hello is not defined!")
        raise

if __name__ == "__main__":
    main()
