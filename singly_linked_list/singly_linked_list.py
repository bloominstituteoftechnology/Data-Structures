# TODO a class that represents the individual elements in our linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self, first_node=None):
        # what attributes do we need?
        self.head = first_node
        self.tail = first_node

    def add_to_head(self, value):
        # create a new Node
        new_node = Node(value)
        if self.head is None:
            # update head & tail attributes
            self.head = new_node
            self.tail = new_node
        else:
            # set next_node of my new Node to the head
            new_node.set_next_node(self.head)
            # update the head attribute
            self.head = new_node

    def add_to_tail(self, value):
        # create a new Node
        new_node = Node(value)
        # 1. LL is empty
        if self.head is None:
            # update head & tail attributes
            self.head = new_node
            self.tail = new_node
        # 2. LL is NOT empty
        else:
            # update next_node of our tail
            self.tail.set_next_node(new_node)
            # update self.tail
            self.tail = new_node

    def remove_head(self):
        # cases to consider?
        # empty list
        if self.head is None:
            return None
        # else - return the VALUE of the old head
        else:
            ret_value = self.head.get_value()
            # list with 1 element
            if self.head == self.tail:
                self.head = None
                self.tail = None
            # list with +2 elements
            else:
                self.head = self.head.get_next_node()
        return ret_value

    def remove_tail(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        else:
            value = self.tail.get_value()
            current = self.head
        while current.get_next_node() != self.tail:
            current = current.get_next_node()
        self.tail = current
        self.tail.set_next_node(None)
        self.tail = current
        return value

    def contains(self, value):
        # loop through LL until next pointer is None
        cur_node = self.head
        while cur_node is not None:
            # if we find 'value'
            if cur_node.get_value() == value:
                # return True
                return True
            # return False
            return False

    def get_max(self):
        current = self.head

        if(self.head == None):
            return None
        else:
            # Initializing max with head's value
            max = self.head.value

            while current is not None:
                # If current node's value is greater than max
                # Then, replace value of max with current node's value
                if(max < current.value):
                    max = current.value
                current = current.get_next_node()
            print("Maximum value: " + str(max))