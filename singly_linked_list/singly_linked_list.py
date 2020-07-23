class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next #if next is not None else None
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None: 
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
            
    def remove_from_tail(self):
        if self.tail is None and self.head is None:
            return
            
        current = self.head
        
        while current.get_next() is not self.tail:
            current = current.get_next()
        
        val = self.tail.get_value()
        self.tail = current
        return val
        
    def remove_head(self):
        if self.tail is None and self.head is None:
            return 
        if not self.head.get_next():
            head = self.head
            self.head = None
            return head.get_value()
        val = self.head.get_value()
        self.head = self.head.get_next()
        return val
    
    def contains(self, value):
        if not self.head:
            return False
        
        current = self.head
        while current:
            
            if current.get_value() == value:
                return True
            
            current = current.get_next()
        return False
        
    def get_max(self):
        # if we do not have a head
        if not self.head:
            return None
        
        if self.head is not None:
            current = self.head
            next_head = self.head.get_next()
            
        if current.value > next_head:
            return current
        
newThing = LinkedList()
print(newThing.get_max())