"""
Concept: Dictionaries (Merging with | Operator)

What:
Python 3.9+ introduced the `|` operator for merging dictionaries.
`dict1 | dict2` creates a NEW dictionary with all items from both.
If keys overlap, values from the RIGHT dictionary (dict2) win.

Why:
Merging dictionaries is common when combining configuration defaults with
user overrides, or aggregating data from multiple sources.

How:
    default = {"theme": "light", "font_size": 12}
    user = {"theme": "dark"}

    # Merge: user settings override defaults
    config = default | user
    # Result: {"theme": "dark", "font_size": 12}

    # The |= operator updates in-place
    default |= user
    # default is now {"theme": "dark", "font_size": 12}

    # Pre-3.9 alternative: {**dict1, **dict2}
    config = {**default, **user}

Task:
Merge `user_config` INTO `default_config` using the `|` operator.
User settings should override defaults (so user_config goes on the right).
"""


def main():
    default_config = {"theme": "light", "notifications": True}
    user_config = {"theme": "dark"}

    # TODO: Merge user_config into default_config using |
    # User settings should override defaults
    config = {}

    # Verification
    if len(config) == 0:
        raise Exception("config is empty! Merge using: default_config | user_config")

    if config.get("theme") != "dark":
        raise Exception(
            f"Expected theme to be 'dark' (from user_config), got '{config.get('theme')}'\n"
            "Make sure user_config is on the RIGHT side of |"
        )

    if config.get("notifications") is not True:
        raise Exception(
            f"Expected notifications to be True (from default_config), got {config.get('notifications')}\n"
            "The merged dict should have keys from BOTH dictionaries."
        )

    print("Dictionary merging successful!")


if __name__ == "__main__":
    main()
