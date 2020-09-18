# TODO a class that represents the individual elements in our LL

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
        new_node = Node(value)
        if self.head is None:
            # update head & tail attributes
            self.head = new_node
            self.tail = new_node
        else:
            # set next_node of my new Node to the head
            new_node.set_next_node(self.head)
            # update head attribute
            self.head = new_node

    def add_to_tail(self, value):
        # create new Node
        new_node = Node(value)
        # 1 LL is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # 2 LL is NOT empty
        else:
            self.tail.set_next_node(new_node)

            self.tail = new_node

    def remove_head(self):
        # empty LinkedList
        if self.head is None:
            return None
        # else, return value of old head
        else:
            ret_value = self.head.get_value()
            # list with 1 element
            if self.head == self.tail:
                self.head = None
                self.tail = None
            # list with 2 elements
            else:
                self.head = self.head.get_next_node()
            return ret_value


    def remove_tail(self):
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value

        else:
            value = self.tail.get_value()
            current_node = self.head

            while current_node.get_next_node() != self.tail:
                current_node = current_node.get_next_node()

            self.tail = current_node
            self.tail.set_next_node(None)
            return value





    def contains(self, value):
        cur_node = self.head
        while cur_node is not None:
            # if we find 'value'
            if cur_node.get_value() == value():
                return True
        return False

    def get_max(self, value):
        pass
        # TODO: