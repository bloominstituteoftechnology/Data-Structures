class Node:
    # next node will be reference to another Noide in list
    def _init_(self, value, next_node=None):
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
        # wrap the value in a new node
        new_node = Node(value)
        # 1 what if our linked list is empty
        # how do we check if linked list is empty
        if not self.head and not self.tail:
            # if our less is empty then node we add will be head and tail
            self.head = new_node
            self.tail = new_node
            # 2. what if our linked list is not empty
        else:
            # new value should be added to tail
            # update the tail nodes next o refer to new node
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        # 1. what if our linked list is empty
        if not self.head and not self.tail:
            return None
        # 2. what if our linked list has one node
        if self.head == self.tail:
            old_head = self.head
            # now we can set both head and tail to none
            self.head = None
            self.tail = None
            return old_head.get_value()
        # 3. what if our linked list has more than one node
        else:
            # set the list's head reference to refer head node's next node
            old_head = self.head
            self.head = self.head.get_next()
            return old_head.get_value()

    def contain(self, value):
        # make sure we have elements in the list to traverse
        if not self.head and not self.tail:
            return None
        current = self.head

        # keep traversing while we're at a valid node
        while current:
            if current.get_value() == value:
                return True
            # update our current pointer
            current = current.get_next()
        # we've tranversed the entire list and our value was not found
        return False
