"""
Concept: Dictionaries (Adding/Updating)

What:
You can add new key-value pairs or update existing ones using square bracket
notation: `dict[key] = value`

Why:
Dictionaries are mutable - you'll often need to add or update entries as your
program runs, like adding new users, updating scores, or modifying settings.

How:
    prices = {"apple": 0.50, "banana": 0.30}

    # Add a new key
    prices["orange"] = 0.80
    # prices is now {"apple": 0.50, "banana": 0.30, "orange": 0.80}

    # Update an existing key
    prices["apple"] = 0.55
    # prices is now {"apple": 0.55, "banana": 0.30, "orange": 0.80}

    # Alternative: .update() for multiple items
    prices.update({"grape": 1.00, "apple": 0.60})

Task:
Add "orange" with a price of 0.80 to the `prices` dictionary.
"""


def main():
    prices = {"apple": 0.50, "banana": 0.30}

    # TODO: Add "orange" with price 0.80

    # Verification
    if "orange" not in prices:
        raise Exception("'orange' is not in prices! Add it: prices['orange'] = 0.80")

    if prices["orange"] != 0.80:
        raise Exception(f"Expected orange price to be 0.80, got {prices['orange']}")

    # Make sure original items are still there
    if prices.get("apple") != 0.50 or prices.get("banana") != 0.30:
        raise Exception("Don't modify the existing prices!")

    print("Successfully added orange to prices!")


if __name__ == "__main__":
    main()
