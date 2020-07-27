class Node:
    def __init__(self, value = None, next = None, next_node = None):
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
        # 1. Create new node from value
        new_node = Node(value, None)
        # 2. Check if list is empty
        if not self.head:
            # 3. Create a new node with value arg
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
            
    def remove_head(self):
        if not self.head:
            return None
        # If head has no next...
        if not self.head.get_next:
            head = self.head
            # Set head reference to None
            self.head = None
            # Set tail reference to None
            self.tail = None
            return head.get_value
        value = self.head.get_value
        self.head = self.head.get_next()
        return value