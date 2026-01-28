
# RECURSION (NESTED STRUCTURES)
# =============================
#
# What: Using recursion to traverse nested data structures like lists of lists.
#
# Why:  Data often comes in arbitrary depths (e.g., JSON, file systems).
#
# How:  Check if an item is a list. If so, recurse. If not, process it.
#       isinstance(item, list) check is key.
#
# Task:
# 1. Define `flatten(nested_list)` that takes a list containing integers
#    and other lists (arbitrarily deep) and returns a single flat list of integers.
#    Input: [1, [2, [3, 4], 5], 6]
#    Output: [1, 2, 3, 4, 5, 6]

def flatten(nested_list):
    result = []
    # TODO: Iterate over nested_list.
    # If item is an integer, append to result.
    # If item is a list, extend result with flatten(item).
    return result

def test_flatten():
    inp = [1, [2, [3, 4], 5], 6]
    expected = [1, 2, 3, 4, 5, 6]
    assert flatten(inp) == expected, f"Expected {expected}, got {flatten(inp)}"
    
    inp2 = [[[1], 2], [3]]
    assert flatten(inp2) == [1, 2, 3], "Deep nesting failed"
    
    assert flatten([]) == [], "Empty list failed"

if __name__ == "__main__":
    test_flatten()
    print("Recursion list flattening passed!")
