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
        # if self.head is not None, so if the LinkedList is not empty:
        if self.head is not None:
            # Create a node with the value argument and set self.tail.next_node equal to that
            self.tail.next_node = Node(value)
            # Assign the value of self.tail.next_node to self.tail
            self.tail = self.tail.next_node
        # if self.head is none (so the LinkedList is empty):
        else:
            # Create a node with the value argument and set self.tail and self.head to that
            self.tail = Node(value)
            self.head = self.tail

    def remove_head(self):
        # if self.head is not None (so if the LinkedList is not empty):
        if self.head is not None:
            # Assign the value of the current head to variable head
            head = self.head.value
            # Set the value of self.head.next_node to self.head
            self.head = self.head.next_node
            # Return the now removed head
            return head
        # if there is no head, return None
        else:
            self.tail = None
            return None

    def contains(self, target):
        # assign the value of the current head to variable current_node
        current_node = self.head
        # while the current_node is not None:
        while current_node is not None:
            # return true if the value of the current node equals the target
            if current_node.value == target:
                return True
            # if it does not, assign the value of current_node.next_node to current_node
            else:
                current_node = current_node.next_node
        # if it goes through the entire list and finds nothing, return False
        return False

    def get_max(self):
        # if current head equals None, return None
        if self.head is None:
            return None
        # assign the value of the current head to variable current_node
        current_node = self.head
        # assign the value of the current node to variable current_max
        current_max = current_node.value
        # while the current node is not equal to None:
        while current_node is not None:
            # if the current head's value is greater than the current max:
            if current_node.value > current_max:
                # assign the value of the current head to the variable current_max
                current_max = current_node.value
            # assign the value of the current head's next node to the variable for current node
            current_node = current_node.next_node
        # return current_max
        return current_max
