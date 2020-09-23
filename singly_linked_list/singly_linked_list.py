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
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(self.value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next_node(self.head)

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node

    def remove_head(self):
        if self.head is None:
            return None
        else:
            ret_value = self.head.get_value()
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else: 
                self.head = self.head.get_next_node()
            return ret_value

    def remove_tail(self):
        # TODO
        if self.tail is None:
            return None
        ret_value = self.tail.get_value()

        if self.head == self.tail:
            self.tail = None
            self.head = None
        else:
            cur_node = self.head
            while cur_node.get_next_node() is not self.tail:
                cur_node = cur_node.get_next_node()
            cur_node.set_next_node(None)
            self.tail = cur_node
        return ret_value

    def contains(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.get_value() == value:
                return True
            else:
                return False

    def get_max(self):
        # TODO 
        pass