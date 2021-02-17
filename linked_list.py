class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def insert_at_head(self, data):
        temp_node = Node(data)
        temp_node.next_node = self.head
        self.head = temp_node
        return self.head

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def print_list(self):
        if self.isEmpty():
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_node
        print(temp.data, "-> None")
        return True