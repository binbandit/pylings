"""
Concept: Doubly Linked Lists

What:
A doubly linked list is like a singly linked list, but each node has
pointers to BOTH the next AND previous nodes. This allows traversal
in both directions.

    None <- [prev|data|next] <-> [prev|data|next] <-> [prev|data|next] -> None
                   ^                                          ^
                 head                                       tail

Why:
- Can traverse backward (singly linked lists cannot)
- Deleting a node is O(1) if you have a reference to it
- Used in: browser history (back/forward), undo/redo, LRU cache
- Keeping a `tail` pointer makes append() O(1) instead of O(n)

How:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None  # NEW: pointer to previous node

    # When appending:
    new_node.prev = old_tail    # Link new node back to old tail
    old_tail.next = new_node    # Link old tail forward to new node
    self.tail = new_node        # Update tail pointer

Task:
1. Add `self.prev = None` to the Node class
2. Implement `DoublyLinkedList.append(data)` - remember to set BOTH links!
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        # TODO: Add self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Tracking tail makes append O(1)!

    def append(self, data):
        """Add a new node at the end. Must set both next and prev pointers!"""
        # TODO: Implement append for doubly linked list
        # 1. Create new node
        # 2. If list is empty: set both head and tail to new node
        # 3. Otherwise:
        #    - new_node.prev = self.tail (link back to old tail)
        #    - self.tail.next = new_node (link old tail forward)
        #    - self.tail = new_node (update tail)
        pass

    def forward(self):
        """Traverse head to tail, return list of values."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def backward(self):
        """Traverse tail to head, return list of values."""
        result = []
        current = self.tail
        while current:
            result.append(current.data)
            current = current.prev
        return result


def main():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)

    # Test forward traversal
    fwd = dll.forward()
    if fwd != [1, 2, 3]:
        raise Exception(
            f"Forward traversal failed: expected [1, 2, 3], got {fwd}\n"
            "Check your append() implementation."
        )

    # Test backward traversal
    bwd = dll.backward()
    if bwd == []:
        raise Exception(
            "Backward traversal returned empty list!\n"
            "Did you add self.prev to Node and set it in append()?"
        )

    if bwd != [3, 2, 1]:
        raise Exception(
            f"Backward traversal failed: expected [3, 2, 1], got {bwd}\n"
            "Make sure you're setting new_node.prev = self.tail in append()"
        )

    # Verify structure
    if dll.head.prev is not None:
        raise Exception("head.prev should be None!")

    if dll.tail.next is not None:
        raise Exception("tail.next should be None!")

    print("List: None <- 1 <-> 2 <-> 3 -> None")
    print("Forward:  [1, 2, 3]")
    print("Backward: [3, 2, 1]")
    print("Doubly linked list implementation verified!")


if __name__ == "__main__":
    main()
