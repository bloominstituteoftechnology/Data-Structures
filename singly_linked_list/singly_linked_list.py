# Imports

#* Node Class

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.new_next = new_next


#* Linked List Class

class LinkedList:
    def __init__(self):
        self.head = None

def add_to_tail(self, data):
    new_node = Node(data)
    new_node.set_next(self.head)
    self.head = new_node

def tail_remove_head(self, data):
    current = self.head
    previous = None
    found = False

    while current and found is False:
        if current.get_data()==data:
            found = True
        else:
            previous = current
            current = current.get_next()
    
    if previous is None:
        self.head = current.get_next()
    else:
        previous.set_next(current.get_next())

def get_max():
    pass