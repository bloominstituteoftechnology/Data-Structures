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

    def __str__(self):
        return f"{self.head}, {self.tail}"

    def add_to_tail(self, value):
        next_node = Node(value)

        if not self.head:
            self.head = next_node
            self.tail = next_node
        else:
            self.tail.set_next(next_node)
            self.tail = next_node

    def remove_head(self):
        if self.head:
            if self.head.get_next() is None:
                temp_head = self.head
                self.head = None
                self.tail = None
                return temp_head.get_value()
            else:
                temp_head = self.head
                self.head = self.head.get_next()
                return temp_head.get_value()
        else:
            return None

    def contains(self, value):
        curr = self.head
        while curr:
            if curr.get_value() == value:
                return True
            curr = curr.get_next()
        return False

    def get_max(self):
        curr = self.head
        max_value = None
        while curr:
            if max_value is None or curr.get_value() > max_value:
                max_value = curr.get_value()
            curr = curr.get_next()
        return max_value


ll = LinkedList()
ll.add_to_tail("Brian")
ll.add_to_tail("Shawn")
ll.add_to_tail("Aaron")
# print(ll.contains("Brian"))
# print(ll.get_max())
# print(ll.remove_head())
