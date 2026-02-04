"""
Concept: The __name__ == "__main__" Guard

When Python runs a file directly, it sets the special variable `__name__` to
"__main__". When a file is imported as a module, `__name__` is set to the
module's name instead.

This allows you to write code that only runs when the file is executed directly:

    if __name__ == "__main__":
        # This code only runs when the file is executed directly
        # It does NOT run when the file is imported
        main()

Why is this important?
1. You can have test code that doesn't run when importing
2. You can create files that work both as importable modules AND standalone scripts
3. It prevents unwanted side effects when importing

Task:
The code below has a print statement running at the global level, which means
it runs even when this file is imported! Move it inside the main() function
or inside the `if __name__ == "__main__":` block.

When you run this file directly, you should see:
    "I am main!"

You should NOT see "I am running as global code!" because that's bad practice.
"""

# TODO: This print statement runs even when the module is imported!
# Move this line so it only runs when the script is executed directly.
# Either put it inside main() or inside the if __name__ == "__main__" block.
print("I am running as global code!")


def main():
    print("I am main!")


# This verification code checks that you fixed the issue
def _verify():
    """Verify that global code was removed."""
    import ast
    import inspect

    # Get the source of this module
    source = inspect.getsource(__import__(__name__))
    tree = ast.parse(source)

    # Check for print calls at module level (outside functions)
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            if isinstance(node.value.func, ast.Name) and node.value.func.id == "print":
                # Check if it's the problematic print
                if node.value.args and isinstance(node.value.args[0], ast.Constant):
                    if "global" in str(node.value.args[0].value).lower():
                        raise AssertionError(
                            "Found a print statement with 'global' at module level!\n"
                            "Move it inside main() or inside the if __name__ == '__main__' block."
                        )


if __name__ == "__main__":
    _verify()
    main()
    print("Exercise completed successfully!")
