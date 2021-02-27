class TrieNode:
    def __init__(self, char=""):
        self.children = [None]
        self.is_end_word = False
        self.char = char

    def mark_as_leaf(self):
        self.is_end_word = True

    def unmark_as_leaf(self):
        self.is_end_word = False
