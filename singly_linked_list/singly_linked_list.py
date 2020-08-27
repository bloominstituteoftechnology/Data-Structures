# Imports

#* Node Class

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        
        self.next_node = new_next


#* Linked List Class

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value): #* add_to_tail
        new_node = Node(value, None)

        if not self.head:
            self.head = new_node
            self.tail = new_node
       
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def contains(self, value): #* contains
        if not self.head:
            return False

        current = self.head
        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False

    def remove_head(self): #* remove_head
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

    def remove_tail(self): #* remove_tail

        if not self.head:
            return None

        if self.head is self.tail:
            value = self.tail
            self.tail = None
            self.head = None

            return value.get_value()

        current = self.head
        while current.get_next() is not self.tail:
            current = current.get_next()

    def get_max(self): #* get_max
        if not self.head:
            return None

        max_value = self.head.get_value()
        current = self.head.get_next()

        while current:

            if current.get_value() > max_value:
                max_value = current.get_value()

            current = current.get_next()
        return max_value

#* PASSED ALL TESTS