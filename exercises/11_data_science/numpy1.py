"""
Concept: Data Science (Numpy Arrays)
Numpy provides powerful N-dimensional arrays. Unlike lists, mathematical operations on arrays apply element-wise.

Task: Create numpy arrays and perform element-wise multiplication.
"""

import numpy as np

def main():
    # FIX ME: Create a numpy array with values [1, 2, 3]
    # arr = np.array([1, 2, 3])
    arr = None
    
    if arr is None or not isinstance(arr, np.ndarray):
        raise Exception("Not a numpy array!")
        
    if arr.tolist() != [1, 2, 3]:
        raise Exception("Array content is wrong!")
        
    # FIX ME: Multiply every element by 2
    # doubled = arr * 2
    doubled = arr
    
    if doubled.tolist() != [2, 4, 6]:
        raise Exception("Did not multiply by 2!")

    print("Numpy arrays verified!")

if __name__ == "__main__":
    main()
