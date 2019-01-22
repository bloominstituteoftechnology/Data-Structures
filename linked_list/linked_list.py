"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node

        else:
            self.tail.set_next(node)
            self.tail = node

    def remove_head(self):
        # Check if the head is None
        if self.head is not None:
            new_head = self.head.next_node
            del(self.head)
            self.head = new_head

    def contains(self, value):
        curr_node = self.head
        while True:
            if curr_node is None:
                return False
            elif curr_node.value == value:
                return True
            else:
                curr_node = curr_node.next_node

    def get_max(self):
        pass


# ll = LinkedList()
# ll.add_to_tail(6)
# print(ll.head.value)
# ll.add_to_tail(1)
# print(ll.tail.value)
# print(ll.contains(2))
# print(ll.contains)
# print()
