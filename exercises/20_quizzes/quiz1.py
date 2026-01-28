"""
Quiz: The Book Store System

Goal: Combine Lists, Dictionaries, Loops, and Functions.

Scenario:
You are building a simple checkout system for a bookstore.
1. You have an `inventory` dictionary: keys are book titles, values are prices.
2. You have a `cart` list: a list of book titles the customer wants to buy.
3. You need to calculate the `total_cost`.
4. If a book in the cart is not in the inventory, print a warning and skip it.
"""

def calculate_total(inventory, cart):
    total = 0
    
    # FIX ME: Iterate through cart
    # Look up price in inventory
    # Add to total
    # If missing, print "Book not found: [title]"
    
    return total

def main():
    inventory = {
        "Python 101": 30.00,
        "Rust for Dummies": 45.50,
        "The Pragmatic Programmer": 50.00
    }
    
    cart = [
        "Python 101",
        "The Pragmatic Programmer",
        "Nonexistent Book", # Should warn
        "Python 101" # Buying a second copy
    ]
    
    # Expected: 30 + 50 + 30 = 110.00
    
    cost = calculate_total(inventory, cart)
    
    if cost != 110.00:
        raise Exception(f"Expected $110.00, got ${cost}")
        
    print("Quiz 1 Passed!")

if __name__ == "__main__":
    main()
