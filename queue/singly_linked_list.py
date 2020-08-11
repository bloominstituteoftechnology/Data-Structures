class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

    def remove_head(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return value

    def remove_tail(self):
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            # store the node, we are going to remove value
            val = self.head.get_value()

            self.head = None
            self.tail = None
            return val
        # otherwise, the linked list has more than one node
        else:
        # store the last Node's value in another variable so we can return it
            val = self.tail.get_value()
        # we need to set 'self.tail' to the second to last Node
        # the only way we can do this, is by traversing the whole linkedlist from beginning

        # starting from the head, we'll traverse down to the second-to-last Node
        # init another reference to keep track of where we are in the linked list as were iterating
        current = self.head
        # keep iterating until the node after 'current' is tail
        while current.get_next() != self.tail:

            # keep iterating
            # set current to its own next
            current = current.get_next()

        # set 'self.tail' to 'current'
        self.tail = current

        # set the new tail's next_node to None
        self.tail.set_next(None)
        return val
