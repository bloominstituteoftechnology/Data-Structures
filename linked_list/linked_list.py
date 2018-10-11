"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # base case if list is empty:
        if self.head is None:
            add_node = Node(value)
            self.head = add_node
            self.tail = add_node
        # add node
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def remove_head(self):
        # removes and returns the head node so you need to return self.head
        store = self.head
        # base case:
        if store is None:
            return "Noting to remove"
        # If there is only one element in the list.
        elif store == self.tail:
            store = self.head
            self.head = None
            self.tail = None
            return store
        else:
            self.head = self.head.next
            return store.value

    def contains(self, value):
        # search through the list and return true if matching value is found, base case if head contains something
        test = self.head
        while test:
            if test.value == value:
                return True
            else:
                test = test.next
        return False

    def get_max(self):
        if self.head is None:
            return None
        else:
            max = self.head.value
            test = self.head
            while test:
                if test.value > max:
                    max = test.value
                else:
                    test = test.next
            return max
