# Implement Node Class

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value

