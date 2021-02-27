class TrieNode:
    def __init__(self, char=""):
        self.children = [None]
        self.is_end_word = False
        self.char = char

    def mark_as_leaf(self):
        self.is_end_word = True

    def unmark_as_leaf(self):
        self.is_end_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_index(self, t):
        return ord(t) - ord("a")

    def insert(self, key):
        pass

    def search(self, key):
        pass

    def delete(self, key):
        pass