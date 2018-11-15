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
            self.tail = new_node
            return
        else:
            self.tail.set_next(
                new_node
            )  # sets the 1st node to current node, providing connection
            self.tail = new_node  # instantiates new node, new next_node is now None
            return

    def remove_head(self):
        prev_head = self.head
        if prev_head == None:  # if no nodes exists
            return None
        elif (
            prev_head == self.tail
        ):  # if only 1 node exists where head and tail are same
            self.head = None
            self.tail = None
            return prev_head.value
        else:
            self.head = self.head.get_next()  # set the next node as the current head
            return prev_head.value

    def contains(self, value):
        current_node = self.head
        if current_node == None:  # if no nodes exists
            return False
        else:
            while current_node is not None:  # if node exists
                if (
                    current_node.value == value
                ):  # if value of current node matches argument value
                    return True
                current_node = (
                    current_node.get_next()
                )  # if value not matched, go to the next node
            return False  # no node has that argument value

    def get_max(self):
        pass
