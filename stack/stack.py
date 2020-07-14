"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

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
        # Create the Node from the value
        new_node = Node(value)

        if self.head is None and self.tail is None:
            # have both head and tail refer to a single node
            self.head = new_node
            self.tail = new_node
        else:
            # set the old tail's next to refer to the new Node
            self.tail.set_next(new_node)
            # reassign self.tail to refer to the new Node
            self.tail = new_node

    def remove_head(self):
        # if we have an empty linked list
        if self.head is None and self.tail is None:
            return

        if not self.head.get_next():
            head = self.head
            # delete the linked list's head reference
            self.head = None
            self.tail = None
            return head.get_value()

        val = self.head.get_value()
        # set self.head to the Node after the head
        self.head = self.head.get_next()
        return val

    def remove_tail(self):
        # if we have an empty linked list
        if self.head is None:
            return

        current = self.head

        while current.get_next() and current.get_next() is not self.tail:
            current = current.get_next()

        #set the tail to be None
        val = self.tail.get_value()
        # move self.tail to the Node right before
        self.tail = current
        # remove new tail's reference to the old tail
        self.tail.set_next(None)
        return val

    def contains(self, value):
        if not self.head:
            return False

        # get a reference to the node we're currently at
        current = self.head

        # check to see if we're at a valid node
        while current:
            # return True if the current value we're lookin at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def get_max(self):
        if not self.head:
            return None

        # reference to the largest value we've seen so far
        max_value = self.head.get_value()

        # reference to our current node as we traverse the list
        current = self.head.get_next()

        # check to see if we're still at a valid list node
        while current:
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()
        return max_value


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_tail()
        return None
