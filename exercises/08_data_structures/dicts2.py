"""
Concept: Dictionaries (Access/Assign)
You can access or add items using square bracket notation `dict[key] = value`.

Task: Add "orange" with a price of 0.80 to the `prices` dictionary.
"""

def main():
    prices = {"apple": 0.50, "banana": 0.30}
    
    # FIX ME: Add "orange" with price 0.80
    
    if "orange" not in prices:
        raise Exception("Orange is missing!")
        
    if prices["orange"] != 0.80:
        raise Exception("Wrong price for orange!")

if __name__ == "__main__":
    main()
