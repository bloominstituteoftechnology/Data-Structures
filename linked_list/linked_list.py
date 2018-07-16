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
        newNode = Node(value, self.tail)
        # check if there is a head
        if(self.head == None):
            # no head, so also no tail, make them both equal to new node
            self.head = newNode
            self.tail = newNode
            return
        # otherwise,
        # update the next pointer on the current tail,
        self.tail.next = newNode
        # make the new node the tail
        self.tail = newNode

    def remove_head(self):
        if(self.head == None):
            return None

        # get a copy of the head
        head = self.head

        # check if the nex node is None
        if(head.next == None):
            self.head = None
            self.tail = None
        else:
            # assign the next node as the new head
            self.head = head.next

        # return the value if you want
        return head.value

    def contains(self, target):
        current = self.head

        while current is not None:
            if current.value == target:
                return True
            current = current.next_node
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
