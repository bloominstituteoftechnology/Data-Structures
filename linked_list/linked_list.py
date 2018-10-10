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
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = Node(value)
            self.tail = self.tail.next_node

    def remove_head(self):
        temp = self.head
        if temp is None:
            return None
        elif temp == self.tail:
            temp = self.head
            self.head = None
            self.tail = None
            return temp.value
        else:
            self.head = self.head.next_node
            return temp.value

    def contains(self, value):
        temp = self.head
        while temp:
            if temp.value == value:
                return True
            temp = temp.next_node
        return False

    def get_max(self):
        if self.head is None:
            return None
        else:
            list_max = self.head.value
            temp = self.head
            while temp:
                if temp.value > list_max:
                    list_max = temp.value
                temp = temp.next_node
            return list_max
