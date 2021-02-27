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
        if key is None:
            return

        key = key.lower()
        current_node = self.root
        index = 0

        for level in range(len(key)):
            index = self.get_index(key[level])

            if current_node.children[index] is None:
                current_node.children[index] = TrieNode(key[level])
                print(key[level] + "inserted")

            current_node = current_node.children[index]

        current_node.mark_as_leaf()
        print("'" + key + "' inserted")

    def search(self, key):
        if key is None:
            return False

        for level in range(len(key)):
            index = self.get_index(key[level])
            if current_node.children[index] is None:
                return False
            current_node = current_node.children[index]

        if current_node is not None and current_node.is_end_word:
            return True

        return False

    def delete(self, key):
        pass