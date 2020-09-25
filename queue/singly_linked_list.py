# Todo a class that represents the individual eles in our LL
import sys


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
        # what attributes do we need?
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        # create a new node
        new_node = Node(value)
        if self.head is None:
            new_node = Node(value)
            # update head and tail attributes
            self.head = new_node
            self.tail = new_node
        else:
            # set next_node of my new node to the Head
            new_node.set_next(self.head)
            # update the head attribute
            self.head = new_node

    def add_to_tail(self, value):
        # TODO
        # create a new node
        new_node = Node(value)
        # 1. LL is empty
        if self.head == None:
            # update head and tail attribution
            self.head = new_node
            self.tail = new_node
        # 2. LL is not empty
        else:
            self.tail.set_next(new_node)
            # update next_node of our tail
            self.tail = new_node

    def remove_head(self):
        # TODO
        if self.head is None:
            return None
        # list with one thing
        else:
            ret_value = self.head.get_value()
            if self.head == self.tail:
                self.head = None
                self.tail = None
        # none empty list - return the value of the old head.
            else:
                self.head = self.head.get_next()
        return ret_value

    def remove_tail(self):
        # if ll is not empty
        if self.head is None:
            return None
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val

        current = self.head
        while current.get_next() != self.tail:
            current = current.get_next()
        # right before self.tail
        val = current.get_next().get_value()
        self.tail = current
        return val

    def contains(self, value):
        # loop through LL until next point is none
        cur_node = self.head
        while cur_node:
            # if we find 'value'
            if cur_node.get_value() == value:
                return True
                # return True or false
            # if we don't find value
        return False

    def get_max(self):
        #list is empty
        if self.head is None:
            return
        if self.head == self.tail:
            return self.head.get_value()
            # loop from head to tail
        high = -sys.maxsize
        current = self.head
        while current:
            if high < current.get_value():
                high = current.get_value()
                current = current.get_next()
            else:
                current = current.get_next()
        return high
