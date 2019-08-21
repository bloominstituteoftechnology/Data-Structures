class Node:
    def __init__(self, value=None, next_node = None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class Linklist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length =0

    def add_to_tail(self, value):
        new_node = Node(value,None)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def add_to_head(self, value):
        new_node = Node(value,None)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

    def remove_head(self):
        if self.head:
            remove = self.head.get_value()
            if self.head is self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next()

        return remove

