class Node:
    def __init__(self, value=None, next_node=None):
        # the value at the linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next(self, new_next):
        # set the current node's "next_node" reference to the passed in node (new_next)
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None
        # reference to the tail of the list
        self.tail = None

    def add_to_head(self, value):
        # create a node
        new_node = Node(value)
        # check is list empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        # if there is a head already
        else:
            # "new node" should point to the "current" head of the linked list as its next node (next_node), therefor positioning self ahead of current head node
            new_node.next_node = self.head
            # then we say current head should point to the new node
            self.head = new_node

    def add_to_tail(self, value):
        # create a node
        new_node = Node(value)
        # check is list empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        # if there is a tail already
        else:
            # current tails node "next" should point at our new node
            self.tail.next_node = new_node
            # make the tail our new node
            self.tail = new_node

    def remove_head(self):
        # check if we have a head (node)
        if self.head is None:
            return None
        # if we only have one node (head and tail point to single node)
        if not self.head.get_next_node():
            # get a ref to the head
            head = self.head
            # delete the lists head reference and make sure that tail does not refer to anything (remove head and tail leaving that single node in limbo and it will get collected by garbage collection)
            self.head = None
            self.tail = None
            # return the value
            return head.get_value()

        # otherwise we have more than one element(node) in the list
        value = self.head.get_value()
        # set the head reference to the current nodes "next" node
        self.head = self.head.next_node  # TODO
        return value

    def remove_tail(self):
        # if list is empty
        if not self.head:
            return None
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value

        current = self.head

        while current.get_next_node() is not self.tail:
            current = current.get_next_node()

        value = self.tail.get_value()
        self.tail = current
        return value

    def contains(self, value):
        if not self.head:
            return None
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next_node()

        # if we've gotten here, then the target node isn't in our list
        return False

    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.get_value()
        # reference to our current node as we traverse the list
        current = self.head.get_next_node()
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next_node()
        return max_value
