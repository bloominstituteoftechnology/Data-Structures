"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
#impliment using an array as the underlying storage:
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
       self.storage.append(value)
       self.size += 1 

    def pop(self):
         if not self.storage:
            return None
         else:
            value = self.storage[-1]
            self.storage.remove(value)
            self.size -= 1
            return value

#impliment using a linked list as the underlying storage:


class Node():
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
        new_node = Node(value, None)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_tail(self):
        if not self.head:
            return None
        elif not self.head.get_next():
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        else:
            current = self.head
            prev = current
            while current.get_next() != None:
                prev = current
                current = current.get_next()
            self.tail = prev
            self.tail.set_next(None)
            return current.get_value()

    def remove_head(self):
        if not self.head:
            return None
        elif not self.head.get_next():
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value


    def contains(self, value):
        if not self.head:
            return False
        else:
            current = self.head
            while current:
                if current.get_value() == value:
                    return True
                else:
                    current = current.get_next()
            return False


    def get_max(self):
        if not self.head:
            return None
        else:
            current = self.head
            max_val = current.get_value()
            while current:
                if current.get_value() > max_val:
                    max_val = current.get_value()
                else:
                    current = current.get_next()
            return max_val 


class StackA:
    def __init__(self):
        self.size = 0
        self.storage =[]
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if not self.storage:
            return
        if not self.storage.head:
            return None
        else:
            value = self.storage[-1]
            self.storage.remove(value)
            value = self.storage.tail.get_value()
            self.storage.remove_tail()
            self.size -= 1
            return value
            #return value


