"""
Concept: Typing (Optional and Union)

Sometimes a value might be one of several types, or might be None.

Optional[T] means "either T or None":
    from typing import Optional

    def find_user(user_id: int) -> Optional[str]:
        # Returns a username string, or None if not found
        ...

Union[A, B] means "either A or B":
    from typing import Union

    def parse_id(value: Union[int, str]) -> int:
        # Accepts either an int or a string
        ...

Note: In Python 3.10+, you can use `int | str` instead of `Union[int, str]`
and `str | None` instead of `Optional[str]`.

Task:
Add type hints to the `get_value` function:
1. `key` should be type `str`
2. `default` can be either an int OR None (use Optional[int])
3. Return type can be either int OR str (use Union[int, str])
"""

from typing import Optional, Union


# TODO: Add type hints using Optional and Union
# Hint: Optional[int] means int | None
# Hint: Union[int, str] means int | str
def get_value(key, default):
    """
    Look up a key and return its value.
    Returns the default if key starts with 'missing'.
    """
    data = {
        "count": 42,
        "name": "example",
        "score": 100,
    }

    if key.startswith("missing"):
        return default if default is not None else 0

    return data.get(key, "not found")


def main():
    # Test the function
    result1 = get_value("count", None)
    result2 = get_value("missing_key", 99)
    result3 = get_value("name", None)

    if result1 != 42:
        raise Exception(f"get_value('count', None) should return 42, got {result1}")
    if result2 != 99:
        raise Exception(f"get_value('missing_key', 99) should return 99, got {result2}")
    if result3 != "example":
        raise Exception(
            f"get_value('name', None) should return 'example', got {result3}"
        )

    # Verify type hints
    annotations = get_value.__annotations__

    if not annotations:
        raise Exception(
            "No type hints found!\n"
            "Add type hints for 'key', 'default', and the return type."
        )

    if "key" not in annotations:
        raise Exception("Parameter 'key' needs a type hint.\nIt should be str.")

    if "default" not in annotations:
        raise Exception(
            "Parameter 'default' needs a type hint.\n"
            "It can be an int OR None, so use Optional[int]."
        )

    if "return" not in annotations:
        raise Exception(
            "Add a return type hint.\n"
            "The function can return int OR str, so use Union[int, str]."
        )

    print("Optional and Union types used correctly!")


if __name__ == "__main__":
    main()
