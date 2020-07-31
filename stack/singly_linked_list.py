class Node:
    def __init__(self, value= None, next_node = None):
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

        new_node = Node(value, None)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        if not self.head.get_next():
            head = self.head

            self.head = None
            
            self.tail = None
            return head.get_value()

        value = self.head.get_value()

        self.head = self.head.get_next()
        return value

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
        '''
        If max is tied, returns the first max
        '''
        if not self.head:
            return None

        current = self.head
        largest = current

        while current:
            if current.get_value() > largest.get_value():
                largest = current
            current = current.get_next()
        
        return largest.get_value()

    def get_count(self):
        '''
        Iteratively gets number of elements in the linked list
        '''
        counter = 0
        current = self.head

        while current:
            counter += 1
            current = current.get_next()

        return counter

    def add_to_head(self, value):
        '''
        Adds value to the head of the linked list
        '''

        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
