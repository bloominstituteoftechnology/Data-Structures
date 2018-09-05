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
        if self.tail:
          self.tail.set_next(Node(value))
          self.tail = self.tail.get_next()
        else:
          self.tail = Node(value)
          self.head = self.tail
 
    def remove_head(self):
        if self.head:
          head_stored = self.head.get_value()
          self.head = self.head.get_next()
          return head_stored  

    def contains(self, value):
        current_var = self.head
        while current_var:
          if current_var.get_value() == value:
            return True
          current_var = current_var.get_next()
        return False

    def get_max(self):
        if not self.head:
            return None
            max_value = self.head.value
            # set current to head's 'next'
            current = self.head.get_next()
            while current:
                if current.value > max_value:
                    # update max value
                    max_value = current.value
                current = current.next_node
            return max_value


