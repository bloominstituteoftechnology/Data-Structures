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
        new_tail = Node(value)
        old_tail = self.tail
        
        if self.tail:
            self.tail.next_node = new_tail
        else:
            self.head = new_tail

        self.tail = new_tail

    def remove_head(self):
        if not self.head:
            return None
        
        head = self.head
        self.head = head.next_node

        return head.value

    def contains(self, value):
        if not self.head:
            return None

        current_node = self.head
        found = False

        while not found:
            if current_node == None:
                return False
            
            if value == current_node.value:
                return True
            else:
                if not current_node.next_node:
                    return False
                    
                current_node = current_node.next_node
                continue

            if not current_node.next_node:
                return False
            
    def get_max(self):
        if not self.head:
            return None

        max_value = self.head.value
        current_node = self.head

        while current_node:
            if max_value < current_node.value:
                max_value = current_node.value

            if not current_node.next_node:
                return max_value

            current_node = current_node.next_node
        