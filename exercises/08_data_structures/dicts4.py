"""
Concept: Dictionaries (Safe Access with .get())

What:
Accessing a key with `dict[key]` raises a KeyError if the key doesn't exist.
The `.get(key, default)` method provides safe access - it returns the default
value (or None) if the key is missing, instead of raising an error.

Why:
Real-world data often has missing fields. Using `.get()` prevents crashes and
lets you provide sensible defaults. This is especially important when dealing
with user input, API responses, or configuration files.

How:
    user = {"name": "Alice", "role": "admin"}

    # Unsafe - raises KeyError if key missing
    # email = user["email"]  # KeyError: 'email'

    # Safe - returns None if key missing
    email = user.get("email")          # None

    # Safe with default value
    email = user.get("email", "N/A")   # "N/A"
    role = user.get("role", "guest")   # "admin" (key exists)

    # Chaining .get() for nested dictionaries
    users = {"alice": {"role": "admin"}}
    role = users.get("bob", {}).get("role", "guest")  # "guest"

Task:
1. Get Bob's role safely using `.get()` - assign to `role`
2. Get Charlie's role (who doesn't exist) - should default to "guest"
"""


def main():
    users = {"alice": {"role": "admin"}, "bob": {"role": "user"}}

    # TODO: Get Bob's role safely (Bob exists, so you'll get "user")
    # Hint: users.get("bob", {}).get("role", "guest")
    role = None

    # TODO: Get Charlie's role safely (Charlie doesn't exist, should be "guest")
    role_charlie = None

    # Verification
    if role is None:
        raise Exception("role is None! Use .get() to safely access Bob's role.")

    if role != "user":
        raise Exception(
            f"Bob's role should be 'user', got '{role}'\n"
            "Use: users.get('bob', {{}}).get('role', 'guest')"
        )

    if role_charlie is None:
        raise Exception("role_charlie is None! Use .get() with a default of 'guest'")

    if role_charlie != "guest":
        raise Exception(
            f"Charlie's role should be 'guest' (default), got '{role_charlie}'\n"
            "Charlie doesn't exist, so .get() should return the default."
        )

    print("Safe dictionary access mastered!")


if __name__ == "__main__":
    main()
