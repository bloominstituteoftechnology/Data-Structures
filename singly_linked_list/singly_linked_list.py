class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_data(self):
        return self.value

    def get_next(self):
        return self.next
    
    def set_next(self, new_node):
        self.next = new_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, data):
        new_node = Node(data)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    
    def remove_head(self):
        if not self.head:
            return None
        
        data = self.head.get_data()

        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()
        
        return data
    
    def remove_tail(self):
        if not self.tail:
            return None
        
        data = self.tail.get_data()

        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head

            while current.get_next() != self.tail:
                current = current.get_next()
                
            self.tail = current
        
        return data
    
    def contains(self, data):
        if not self.head:
            return False

        current = self.head

        while current is not None:
            if current.get_data() == data:
                return True
            
            current = current.get_next()
    
        return False
    
    def get_max(self):
        if self.head is None:
            return None

        max_so_far = self.head.get_data()
        current = self.head.get_next()

        while current is not None:
            if current.get_data() > max_so_far:
                max_so_far = current.get_data()

            current = current.get_next()
        
        return max_so_far