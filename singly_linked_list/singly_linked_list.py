
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def traverse_list(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            n = self.head
            while n is not None:
                print(n.value, " ")
                n = n.next

    def add_to_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = new_node
