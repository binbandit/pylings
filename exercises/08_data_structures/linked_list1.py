"""
Concept: Singly Linked Lists

What:
A linked list is a linear data structure where elements are not stored at contiguous memory locations.
Each element (Node) contains data and a pointer (reference) to the next node.

Why:
- Dynamic size (unlike arrays in C/C++, though Python lists are dynamic arrays).
- Efficient insertions/deletions at the beginning.
- Fundamental for understanding pointers and references.

How:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        # Traverse to end
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
```

Task:
1. Implement the `Node` class.
2. Implement `LinkedList.append(value)` to add to the end.
3. Implement `LinkedList.to_list()` to return a Python list of values (for testing).
"""

class Node:
    # FIX ME: Implement __init__ with data and next
    # def __init__(self, data):
    #     self.data = data
    #     self.next = None
    pass

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        # FIX ME: Add data to end of list
        pass
        
    def to_list(self):
        # FIX ME: Traverse and return list of values
        # result = []
        # curr = self.head
        # while curr: ...
        # return result
        return []

def main():
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    
    result = ll.to_list()
    expected = [10, 20, 30]
    
    if result != expected:
        raise Exception(f"Expected {expected}, got {result}")
        
    print("Singly Linked List implementation verified.")

if __name__ == "__main__":
    main()
