class Node: 
    def __init__(self,value):
        self.value = value
        self.next = None
    
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_text): 
        self.next = new_text

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self,value):
        new_node = Node(value)

        if self.tail is None and self.tail is None: 
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if self.head is None and self.tail is None:
            return

        if not self.head.get_next():
            head = self.head
            self.head = head
            self.tail = None
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        if self.head is None and self.tail is None:
            return 

        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val

        else: 
            val = self.tail.get_value()
            current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()


        self.tail = current
        self.tail.set_next(None)
        self.tail = current
        return val

    def length(self):
        return len(self)


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return
        else: 
            removedValue = self.storage.remove_tail()
            self.size -= 1
            return removedValue