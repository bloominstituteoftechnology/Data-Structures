class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)

class SinglyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.length = 1 if node is not Node else 0

    def add_to_head(self, value):
        new_node = Node(value)
        self.length += 1
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete(self, node):
        pass

    def reverse_sll(self):
        pass


def find_middle(sll):
    slow_node = fast_node = sll.head

    while fast_node.next.next is not None:
        slow_node = slow_node.next
        fast_node = fast_node.next.next
    return slow_node
