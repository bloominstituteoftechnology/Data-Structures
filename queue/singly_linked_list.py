class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return f"value = {self.value} next_node = {self.next_node}"

class LinkedList:
    def __init__(self):
        self.tail = None
        self.head = None

    def __str__(self):
        return f"head={self.head} tail={self.tail}"

    def add_to_tail(self, value):
        node = Node(value)
        if self.tail == None:
            self.head = node
        else:
            self.tail.next_node = node

        self.tail = node


    def remove_head(self):
        if self.head == None:
            return None

        node = self.head
        self.head = self.head.next_node
        if self.head == None:
            self.tail = None
             
        return node.value

    def remove_tail(self):
        if self.tail == None:
            return None

        value = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return value
        
        node = self.head
        while node.next_node != self.tail:
            node = node.next_node

        self.tail = node
        self.tail.next_node = None
        
        return value
    


    

    