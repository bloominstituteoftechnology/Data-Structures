class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
       
class Stack:
    def __init__(self):
        self.head = None

    def length(self):
        current = self.head
        length = 0
        while current:
            length = length + 1
            current = current.next
        return length

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped