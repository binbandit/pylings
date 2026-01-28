"""
Concept: Doubly Linked Lists

What:
A doubly linked list is similar to a singly linked list, but each node has a pointer to BOTH the next node and the PREVIOUS node.

Why:
- Allows traversal in both directions.
- Deletion of a node is easier if you have a reference to it (no need to traverse from head to find the previous one).

How:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
```

Task:
1. Implement `Node` with `next` and `prev`.
2. Implement `DoublyLinkedList.append(value)`.
3. Ensure both forward and backward links are set correctly.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        # FIX ME: Add self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # Keeping track of tail makes append O(1)
        
    def append(self, data):
        # FIX ME: Implement append. Remember to set new_node.prev!
        pass
        
    def forward(self):
        res = []
        curr = self.head
        while curr:
            res.append(curr.data)
            curr = curr.next
        return res
        
    def backward(self):
        res = []
        curr = self.tail
        while curr:
            res.append(curr.data)
            curr = curr.prev
        return res

def main():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    
    fwd = dll.forward()
    if fwd != [1, 2, 3]:
        raise Exception(f"Forward traversal failed: {fwd}")
        
    bwd = dll.backward()
    if bwd != [3, 2, 1]:
        raise Exception(f"Backward traversal failed: {bwd}. Did you set .prev and update .tail?")

if __name__ == "__main__":
    main()
