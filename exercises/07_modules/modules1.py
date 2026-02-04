"""
Concept: Importing Modules (Standard Library)

Python comes with "batteries included" - a large standard library of modules
you can import and use. To use code from a module, you must first import it.

The basic import syntax is:
    import module_name

After importing, you access the module's contents using dot notation:
    module_name.function_name()
    module_name.ClassName()

For example, if you import the `math` module:
    import math
    result = math.sqrt(16)  # Access sqrt function via math.

Task:
Import the `datetime` module so you can use `datetime.datetime.now()` to get
the current time.

Hint: The import statement goes at the top of the file (or before you use it).
"""

# TODO: Import the datetime module here


def main():
    # This line needs the datetime module to be imported
    # datetime.datetime is the class, .now() is a method that returns current time
    now = datetime.datetime.now()
    print(f"The current time is: {now}")
    print("Successfully imported the datetime module!")


if __name__ == "__main__":
    main()
