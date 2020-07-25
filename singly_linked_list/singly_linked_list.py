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
        # reference to the head of the list
        self.head = None
        # reference to the tail of the list
        self.tail = None

    def add_to_head(self, value):
        # create a new node
        new_node = Node(value)
        # if list empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # list not empty
        else:
            new_node.set_next(self.head)
            self.head = new_node

    def add_to_tail(self, value):
        # wrap the input value in a node
        new_node = Node(value, None)
        # check if there is no head (i.e., the list is empty)
        if not self.head:
            # if the list is initially empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # we have a non-empty list, add the new node to the tail
        else:
            # set the current tail's next reference to our new node
            self.tail.set_next(new_node)
            # set the list's tail reference to the new node
            self.tail = new_node

    def remove_head(self):
        # return None if there is no head (i.e. the list is empty)
        if not self.head:
            return None
        # if head has no next, then we have a single element in our list
        if not self.head.get_next():
            # get a reference to the head
            head = self.head
            # delete the list's head reference
            self.head = None
            # also make sure the tail reference doesn't refer to anything
            self.tail = None
            # return the value
            return head.get_value()
        # otherwise we have more than one element in our list
        value = self.head.get_value()
        # set the head reference to the current head's next node in the list
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        # if list empty
        if not self.head:
            return None
        # head has no next
        elif not self.head.get_next():
            tail = self.tail
            self.head = None
            self.tail = None
            return tail.get_value()
        # list with next
        else:
            prev = self.head
            curr = prev
            while curr.get_next():
                prev = curr
                curr = curr.get_next()
                if curr == self.tail:
                    prev.set_next(None)
                    self.tail = prev
                    return curr.get_value()

    def contains(self, value):
        if not self.head:
            return False

        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def get_max(self):
        # check if the head is not none
        if not self.head:
            return None
        current_node = self.head
        max_value = self.head.get_value()
        while current_node:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next_node
        return max_value