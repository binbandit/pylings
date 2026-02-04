"""
Concept: Singly Linked Lists

What:
A linked list is a linear data structure where elements (nodes) are connected
by pointers. Each node contains data and a reference to the next node.
Unlike arrays/lists, elements are NOT stored in contiguous memory.

    [data|next] -> [data|next] -> [data|next] -> None
         ^
        head

Why:
- O(1) insertion/deletion at the beginning (lists are O(n))
- Dynamic size with no wasted space
- Foundation for understanding pointers and more complex structures
- Common interview topic!

How:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None  # Pointer to next node

    # Creating a simple linked list manually:
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    # 10 -> 20 -> 30 -> None

Task:
1. Complete the Node class with `data` and `next` attributes
2. Implement `LinkedList.append(data)` to add a node at the end
3. Implement `LinkedList.to_list()` to convert to a Python list
"""


class Node:
    def __init__(self, data):
        # TODO: Store the data
        self.data = None  # Fix this!
        # TODO: Initialize next pointer to None
        self.next = "not_set"  # Fix this!


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a new node with `data` at the end of the list."""
        # TODO: Implement append
        # 1. Create a new Node
        # 2. If list is empty (self.head is None), set head to new node
        # 3. Otherwise, traverse to the last node and set its .next to new node
        pass

    def to_list(self):
        """Convert linked list to Python list for easy testing."""
        # TODO: Traverse the list and collect all data values
        # result = []
        # current = self.head
        # while current is not None:
        #     result.append(current.data)
        #     current = current.next
        # return result
        return []


def main():
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)

    result = ll.to_list()
    expected = [10, 20, 30]

    # Verification
    if result == []:
        raise Exception(
            "to_list() returned empty list!\nDid you implement append() and to_list()?"
        )

    if result != expected:
        raise Exception(
            f"Expected {expected}, got {result}\n"
            "Check your append() and to_list() implementations."
        )

    # Verify Node structure
    if ll.head is None:
        raise Exception("head should not be None after appending!")

    if ll.head.next is None:
        raise Exception("head.next is None - append() isn't linking nodes correctly.")

    print("Linked list: 10 -> 20 -> 30 -> None")
    print("Singly linked list implementation verified!")


if __name__ == "__main__":
    main()
