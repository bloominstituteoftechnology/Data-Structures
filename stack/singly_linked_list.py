class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        # reference to next node
        self.next = next
    
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        # set this node's next reference to the node passed in
        self.next = new_next

class LinkedList:
    def __init__(self, node=None):
        self.head = node
    
    def add_to_tail(self, value):
        new_node = Node(value)

        # if the linked list is empty
        if not self.head:
            self.head = new_node
        else:
            # add node to tail
            # traverse linked list to get to tail
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            # at end of linked list
            current.set_next(new_node)
    
    def remove_from_head(self):
        if not self.head:
            return None
        # if linked list is not empty
        else:
            # return value at current head
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value