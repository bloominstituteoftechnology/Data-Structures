class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node
    
class LinkedList(Node):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def add_to_tail(self, value):
        new_node = Node(value)
        
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    
    def add_to_head(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
    
    def remove_tail(self):
        if self.head is None and self.tail is None:
            return None
        
        if self.head == self.tail:
            retval = self.tail.get_value()
            self.head = None
            self.tail = None
            return retval
        else: 
            current_node = self.head
            while current_node.get_next() != self.tail:
                current_node = current_node.get_next()
            retval = self.tail.get_value()
            self.tail = current_node
            self.tail.set_next(None)
            return retval
        
    def remove_head(self):
        if self.head is None and self.tail is None:
            return None
        
        if self.head == self.tail:
            retval = self.head.get_value()
            self.head = None
            self.tail = None
        else:
            retval = self.head.get_value()
            self.head = self.head.get_next()
        return retval

    def contains(self, value):
        if self.head == None:
            return False
        
        current = self.head
        while current is not None:
            if current.get_value() == value:
                return True
            else:
                current = current.get_next()
        return False