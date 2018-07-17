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
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        if self.tail != None:
            self.tail.next_node = new_node
        self.tail = new_node

    def remove_head(self):
        if self.head == None:
            return None
        removed_value = self.head.value
        new_head = self.head.next_node
        self.head = new_head
        return removed_value

    def contains(self, target):
          # if input value exsist in the list,return True
          # if not, return False
        current_node = self.head

        if current_node == None:
            return False
        if current_node.value == target:
            return True

        while current_node.next_node != None:

            next_node = current_node.next_node
            current_node = next_node
            if current_node.value == target:
                return True

        return False

    def get_max(self):
        current = self.head

        # check if there is a value
        if(current is None):
            return None

        # assign the first value as max
        max = current.value

        while(current is not None):
            print(current.value)
            if(current.value > max):
                max = current.value
            current = current.next_node

        return max
