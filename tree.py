class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

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