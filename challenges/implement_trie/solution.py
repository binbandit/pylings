"""
# Implement Trie (Prefix Tree)

A **Trie** (pronounced as "try") or **prefix tree** is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spell checker.

Implement the `Trie` class:

- `Trie()` Initializes the trie object.
- `void insert(String word)` Inserts the string `word` into the trie.
- `boolean search(String word)` Returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false` otherwise.
- `boolean startsWith(String prefix)` Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.
"""

class Trie:

    def __init__(self):
        # TODO: Initialize root node
        pass

    def insert(self, word: str) -> None:
        # TODO: Insert word
        pass

    def search(self, word: str) -> bool:
        # TODO: Return true if word fully exists
        return False

    def startsWith(self, prefix: str) -> bool:
        # TODO: Return true if prefix exists
        return False
