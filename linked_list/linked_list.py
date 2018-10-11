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
        self.length = 0

    def add_to_tail(self, value):
        # creates a new node and assign it as the head of the list since length is 0
        # when run again would assign next on previous item and set default next to none
        newNode = Node(self, value)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
            self.length += 1
        else:
            self.tail.next_node = newNode
            self.length += 1
            self.tail = newNode

    def remove_head(self):
        pass
# if self.head = true then
# removed_head= LinkedList.head
# LinkedList.head.remove()
# return removed_head

    def contains(self, value):
        pass

    def get_max(self):
        pass
