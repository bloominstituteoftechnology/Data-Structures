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
    def __init__(self, first_node=Node):
        #attributes needed:
        self.head= first_node
        self.tail= first_node
        # what attributes do we need?
    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next_node(self.head)
            self.head = new_node
    def add_to_tail(self, value):
        new_node=Node(value)
        if self.head is None:
            self.head= new_node
            self.tail= new_node
        else:
            self.tail.set_next_node(new_node)
            self.tail= new_node
        

    def remove_head(self):
        if self.head is None:
            return None
        else:
            ret_value= self.head.get_value()
            if self.head== self.tail:
                self.head=None
                self.tail=None
               
            else:
                self.head = self.head.get_next_node()
            return ret_value
    def remove_tail(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
            
    def contains(self, value):
        cur_node = self.head
        while cur_node is not None:
            if cur_node.get_value()== value:
                return True
        return False
    def get_max(self):
        if self.head is None:
            return
        if self.head == self.tail:
            return self.head.get_value()
            # loop from head to tail
        high = -sys.maxsize
        current = self.head
        while current:
            if high < current.get_value():
                high = current.get_value()
                current = current.get_next()
            else:
                current = current.get_next()
        return high    
    def remove_tail(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val

        current = self.head
        while current.get_next() != self.tail:
            current = current.get_next()
        # right before self.tail
        val = current.get_next().get_value()
        self.tail = current
        self.tail.set_next("None")
        return val