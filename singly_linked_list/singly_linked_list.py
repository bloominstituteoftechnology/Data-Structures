class Node:
    def __init__(self, value = None, next_node = None):
        self.value = value
        self.next_node = next_node
        
    def get_value(self):
        return self.value
    
    # def get_next(self):
    #     return self.next_node
    
    # def set_next(self, new_next):
    #     self.next_node = new_next
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_to_tail(self, value):
        # 1. Create new node from value
        new_node = Node(value)
        # 2. Check if list is empty
        if not self.head and not self.tail:
            # 3. Create a new node with value arg
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
            
    def remove_head(self):
        if not self.head:
            return None
        # If head has no next...
        if not self.head.next_node: # Or if self.head.next is None:
            # Set head value reference
            head_value = self.head.value
            # Set head reference to None
            self.head = None
            # Set tail reference to None
            self.tail = None
            return head_value
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value
    
    def contains(self, value):
        if not self.head:
            return False
        current_node = self.head
        while current_node is not None:
            if current_node.get_value() == value:
                return True
            current_node = current_node.next_node
        return False
    
    def get_max(self):
        if not self.head:
            return None
        current = self.head
        max_val = self.head.value
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next_node
        return max_val