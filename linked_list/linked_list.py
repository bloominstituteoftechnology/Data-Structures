"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
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

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head:
            self.tail.set_next(new_node)
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node     
        
    def remove_head(self):
        if self.head:
            if self.tail is self.head:
                self.tail = None
            old_head = self.head
            self.head = self.head.get_next()
            return old_head.value

    def contains(self, value):
        current = self.head
        found = False
        while current and not found:
            if current.get_value() == value:
                found = True
            else:
                current = current.get_next()
        return found        

    def get_max(self):
        if self.head:
            current = self.head
            largest = current.get_value()
            while current:
                value = current.get_value()
                if largest < value:
                    largest = value
                current = current.get_next()
            return largest

