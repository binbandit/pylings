"""
Quiz: Bookstore Checkout System

This quiz combines: Lists, Dictionaries, Loops, Functions, and Conditionals.

Scenario:
You're building a checkout system for a bookstore.
- The `inventory` dict maps book titles to their prices
- The `cart` list contains book titles the customer wants to buy
- A book might appear multiple times in the cart (buying multiple copies)
- Some books in the cart might not exist in inventory

Task:
Implement `calculate_total(inventory, cart)` that:
1. Iterates through each book in the cart
2. If the book exists in inventory, adds its price to the total
3. If the book does NOT exist, prints: "Book not found: {title}"
4. Returns the total cost

Example:
    inventory = {"Python 101": 30.00, "Rust Basics": 45.00}
    cart = ["Python 101", "Unknown Book", "Python 101"]

    calculate_total(inventory, cart)
    # Prints: "Book not found: Unknown Book"
    # Returns: 60.00 (30 + 30)
"""


def calculate_total(inventory, cart):
    """
    Calculate the total cost of books in the cart.

    Args:
        inventory: dict mapping book titles (str) to prices (float)
        cart: list of book titles (str) to purchase

    Returns:
        float: total cost of all valid books in cart
    """
    total = 0.0

    # TODO: Loop through each book title in the cart
    # TODO: Check if the book exists in the inventory
    #       - If yes: add its price to total
    #       - If no: print "Book not found: {title}"
    #
    # Hint: Use `for book in cart:` to iterate
    # Hint: Use `if book in inventory:` to check existence
    # Hint: Use `inventory[book]` to get the price

    return total


def main():
    inventory = {
        "Python 101": 30.00,
        "Rust for Beginners": 45.50,
        "The Pragmatic Programmer": 50.00,
        "Clean Code": 40.00,
    }

    cart = [
        "Python 101",  # $30.00
        "The Pragmatic Programmer",  # $50.00
        "Nonexistent Book",  # Not found (should print warning)
        "Python 101",  # $30.00 (second copy)
    ]

    print("Processing cart...")
    print("-" * 30)

    total = calculate_total(inventory, cart)

    print("-" * 30)

    # Expected total: 30 + 50 + 30 = 110.00
    expected = 110.00

    if total != expected:
        raise Exception(
            f"Total should be ${expected:.2f}, got ${total:.2f}\n\n"
            "Hints:\n"
            "- Loop through each book in the cart\n"
            "- Check if each book exists in inventory\n"
            "- Add the price to total if it exists\n"
            "- Print a warning if it doesn't exist"
        )

    print(f"\nTotal: ${total:.2f}")
    print("\nQuiz 1 passed!")


if __name__ == "__main__":
    main()
