"""
Concept: Environment Variables

Environment variables are key-value pairs stored in your operating system's
environment. Programs can read and write these variables.

Why use environment variables?
- Store configuration without hardcoding
- Keep secrets (API keys, passwords) out of source code
- Change behavior without modifying code

How to use them in Python:
    import os

    # Set an environment variable (for current process only)
    os.environ["MY_VAR"] = "my_value"

    # Get an environment variable (returns None if not found)
    value = os.getenv("MY_VAR")

    # Get with a default value
    value = os.getenv("MY_VAR", "default")

    # Get (raises KeyError if not found)
    value = os.environ["MY_VAR"]

Security tip:
    Never hardcode secrets like API keys or passwords in your code!
    Store them in environment variables and read them at runtime.

Task:
1. Set an environment variable named "APP_MODE" with value "production"
2. Retrieve it using os.getenv() and store in `current_mode`
"""

import os


def main():
    # TODO: Set the environment variable APP_MODE to "production"
    # Hint: os.environ["KEY"] = "value"

    # TODO: Get the value of APP_MODE using os.getenv()
    # Hint: os.getenv("KEY")
    current_mode = None  # TODO: Replace with os.getenv(...)

    # Verification
    if current_mode is None:
        raise AssertionError(
            "current_mode is None!\n"
            "Did you:\n"
            "  1. Set os.environ['APP_MODE'] = 'production'?\n"
            "  2. Retrieve it with current_mode = os.getenv('APP_MODE')?"
        )

    if current_mode != "production":
        raise AssertionError(
            f"Expected current_mode to be 'production', but got '{current_mode}'"
        )

    # Double-check it's actually in the environment
    env_value = os.environ.get("APP_MODE")
    if env_value != "production":
        raise AssertionError(
            "APP_MODE is not set in os.environ!\n"
            "Make sure to set os.environ['APP_MODE'] = 'production'"
        )

    print(f"APP_MODE = {current_mode}")
    print("Successfully used environment variables!")


if __name__ == "__main__":
    main()
