 # a class that represents the individual elements in our LL
 
 
class Node:
    def __init__(self, value=None, next_node=None):
         self.value = value
         self.next_node = next_node
    
    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # what attributes do we need?
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        # create a new Node
        new_node = Node(value)
        if self.head is None:
            # update head and tail attributes
            self.head = new_node
            self.tail = new_node
        else:
            # set next_node of my new Node to the head
            new_node.set_next_node(self.head)
            # update head attribute
            self.head = new_node
    
    def add_to_tail(self, value):
        # create a new Node
        new_node = Node(value)
        # 1. LL is empty
        if self.head is None:
            # update head & tail attributes
            self.head = new_node
            self.tail = new_node

        # 2 LL is NOT empty
        else:
            # update next_node of our tail
            self.tail.set_next_node(new_node)
            # update self.tail
            self.tail = new_node

    def remove_head(self):
        # empty list
        if self.head is None:
            return None
        # else, return Value of the old head
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
        # empty list
        if self.tail is None:
            return None
        # else, return value of the old tail
        elif self.head == self.tail:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            return value
        else:
            # else set head to current
            cur = self.head
            # then while there are nodes afterward
            while cur.get_next_node() != self.tail:
                # change the current node to the next node, iterate
                cur = cur.get_next_node()
            # once the next node is none, set the current node to previous, and add none after it
            value = self.tail.get_value()
            cur.set_next_node(None)
            # set that previous value to the new tail
            self.tail = cur
            # return the tail
            return value

    def contains(self, value):
        # loop through LL until pointer is None
        cur_node = self.head
        while cur_node is not None:
            # if we find 'value'
            if cur_node.get_value() == value:
                return True
            # next_node
            cur_node = cur_node.get_next_node()
        return False

    def get_max(self):
         # empty list
        if self.head is None:
            return None
        # iterate through all elements
        cur_node = self.head
        # set max to first node
        cur_max = self.head.get_value()
        while cur_node is not None:
            # search for higher values
            if cur_node.get_value() > cur_max:
                # set new max
                cur_max = cur_node.get_value()
            # move on to next node
            cur_node = cur_node.get_next_node()
        return cur_max