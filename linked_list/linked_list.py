"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""


class Node:
    def __init__(self, value=None, next_node=None):
        # whatever value you are one
        self.value = value
        # pointer (under the hood is a memory address)
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
        # create a new node
        node = Node(value)
        # if there is a current tail
        if self.tail is not None:
            # set the tail's next to new node
            self.tail.set_next(node)
        # if only one item head and tail are same
        else:
            self.head = node
        # set linked list tail to new node
        self.tail = node

    def remove_head(self):
        # check if head is None
        if self.head is not None:
            # set next to head value (it's the address)
            new_head = self.head.get_next()
            old_head = self.head.get_value()

            # if no new head means there's only one item in list
            if new_head is None:
                self.tail = None
                self.head = None
            # set new head
            self.head = new_head

            return old_head

    def contains(self, value):
        # set current node to head
        curr_node = self.head
        while True:
            if curr_node is None:
                return False
            elif curr_node.value == value:
                return True
            else:
                curr_node = curr_node.next_node

    def get_max(self):
        # if linked list is empty
        if self.head is None:
            return

        # store head in temp variable
        curr_node = self.head

        # if there is only one item in linked list
        if curr_node.next_node is None:
            # that's the biggest!
            return curr_node.get_value()

        # else assign the next node to a temp variable
        next_node = self.head.get_next()

        # Loop through the linked list
        while next_node is not None:
            # check to see if next node is bigger than current
            if curr_node.get_value() < next_node.get_value():
                # switch current node
                curr_node = next_node
            # update to next node -> if None the loop stops
            next_node = next_node.get_next()
        else:
            return curr_node.get_value()
