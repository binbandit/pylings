"""
Concept: Dictionaries (Iteration)
You can iterate over keys, values, or items (both) using `.keys()`, `.values()`, or `.items()`.

Task: Iterate over the dictionary using `.items()` and populate the output list.
"""

def main():
    data = {"a": 1, "b": 2}
    
    # FIX ME: Iterate over keys and values
    output = []
    # for k, v in data.items():
    #     output.append(f"{k}:{v}")
    
    if "a:1" not in output or "b:2" not in output:
        raise Exception("Did not iterate correctly!")

if __name__ == "__main__":
    main()
