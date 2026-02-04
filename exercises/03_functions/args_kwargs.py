"""
args_kwargs.py - *args and **kwargs

Sometimes you want a function to accept any number of arguments:

*args (positional arguments):
    def sum_all(*args):
        return sum(args)  # args is a tuple

    sum_all(1, 2, 3)      # args = (1, 2, 3)

**kwargs (keyword arguments):
    def print_info(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")

    print_info(name="Alice", age=30)  # kwargs = {'name': 'Alice', 'age': 30}

You can combine them:
    def example(required, *args, **kwargs):
        pass

Your task: Modify the `log_message` function to accept:
1. `message` - required first argument
2. `*args` - any additional positional arguments
3. `**kwargs` - any additional keyword arguments
"""


# TODO: Add *args and **kwargs to this function signature
def log_message(message):
    print(f"LOG: {message}")


def main():
    # This should work if you added *args and **kwargs
    try:
        log_message("Error occurred", "file.py", 42, user="admin", level="critical")
    except TypeError as e:
        raise Exception(f"Function signature is wrong: {e}")

    # Verify the function signature
    import inspect

    sig = inspect.signature(log_message)
    params = list(sig.parameters.values())

    has_var_positional = any(p.kind == inspect.Parameter.VAR_POSITIONAL for p in params)
    has_var_keyword = any(p.kind == inspect.Parameter.VAR_KEYWORD for p in params)

    if not has_var_positional:
        raise Exception("Function needs *args (VAR_POSITIONAL parameter)")
    if not has_var_keyword:
        raise Exception("Function needs **kwargs (VAR_KEYWORD parameter)")

    print("*args and **kwargs work correctly!")


if __name__ == "__main__":
    main()
