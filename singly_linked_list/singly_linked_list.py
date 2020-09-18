class Node():
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

    def add_to_head(self, value):
        #create a node from input
        new_node = Node(value, None)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value, None)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_tail(self):
        if not self.head:
            return None
        elif not self.head.get_next():
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        else:
            current = self.head
            prev = current
            while current.get_next() != None:
                prev = current
                current = current.get_next()
            self.tail = prev
            self.tail.set_next(None)
            return current.get_value()

    def remove_head(self):
        if not self.head:
            return None
        elif not self.head.get_next():
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value


    def contains(self, value):
        if not self.head:
            return False
        else:
            current = self.head
            while current:
                if current.get_value() == value:
                    return True
                else:
                    current = current.get_next()
            return False


    def get_max(self):
        if not self.head:
            return None
        else:
            current = self.head
            max_val = current.get_value()
            while current:
                if current.get_value() > max_val:
                    max_val = current.get_value()
                else:
                    current = current.get_next()
            return max_val 