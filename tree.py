class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    #Iterative insert
    def insert(self, data):
        current = self
        parent = None

        while current:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right
        
        if data < parent.data:
            parent.left = Node(data)
        else:
            parent.right = Node(data)

    #Recursive insert
    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
                return
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
                return 
                
class BinarySearchTree:
    def __init__(self):
        self.root = Node(data)

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True


    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    def delete(self, val):
    if val < self.val:  # val is in the left subtree
        if(self.leftChild):
            self.leftChild = self.leftChild.delete(val)
        else:
            print(str(val) + " not found in the tree")
            return None
    elif val > self.val:  # val is in the right subtree
        if(self.rightChild):
            self.rightChild = self.rightChild.delete(val)
        else:
            print(str(val) + " not found in the tree")
            return None
    else:  # val was found
        # deleting node with no children
        if self.leftChild is None and self.rightChild is None:
            self = None
            return None
        # deleting node with right child
        elif self.leftChild is None:
            tmp = self.rightChild
            self = None
            return tmp
        # deleting node with right child
        elif self.leftChild is None:
            tmp = self.rightChild
            self = None
            return tmp
        # deleting a node with two children
        else:
            # first get the inorder successor
            current = self.rightChild
            # loop down to find the leftmost leaf
            while(current.leftChild is not None):
                current = current.leftChild
            self.val = current.val
            self.rightChild = self.rightChild.delete(current.val)

    return self

def _display_aux(node):
    """
    Returns list of strings, width, height,
    and horizontal coordinate of the root.
    """
    # No child.
    if node.rightChild is None and node.leftChild is None:
        line = str(node.val)
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.rightChild is None:
        lines, n, p, x = _display_aux(node.leftChild)
        s = str(node.val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if node.leftChild is None:
        lines, n, p, x = _display_aux(node.rightChild)
        s = str(node.val)
        u = len(s)
#        first_line = s + x * '_' + (n - x) * ' '
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(node.leftChild)
    right, m, q, y = _display_aux(node.rightChild)
    s = '%s' % node.val
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * \
        '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + \
        (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + \
        [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2

def minDepth(root):
    if root == None:
        return True
    flag = True
    first_branch = None
    counter = 1


def sumRootToLeaf(root):
    string = ""
    List = []
    total = 0

    def DFS(root, string):
        nonlocal List
        if root == None:
            List.append(string)
            return
        DFS(root.left, string + str(root.data))
        DFS(root.right, string + str(root.data))

    DFS(root, string)
    for n in List:
        total += int(n, 2)

    return total


head = Node(10)
head.insert(12)
head.insert(8)
head.insert(9)
head.insert(6)
head.insert(7)
head.insert(5)

# head.PrintTree()
print(sumRootToLeaf(head))