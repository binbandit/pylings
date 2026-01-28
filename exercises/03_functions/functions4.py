"""
Concept: Functions (Default Arguments)
Arguments can have default values, effectively making them optional.

Task: Fix the `calculate_area` function. It seems to have a bug in its logic or default value.
"""

def sale_price(price, discount=10):
    return price - discount

def main():
    print(sale_price(100))
    print(sale_price(100, discount=20))
    
    # This line is failing! We need the function to return 80!
    if sale_price(100, 20) != 80:
        raise Exception("Price calculation is wrong!")

if __name__ == "__main__":
    main()
