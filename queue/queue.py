"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#          return self.size

#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def dequeue(self):
#            if not self.storage:
#             return
#            else:
#             value = self.storage[0]
#             self.storage.pop(0)
#             self.size -= 1
#             return value

# impliment using a LinkedList as the underlying storage:
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
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            # otherwise the list must have at least one item in there
        else:
            self.tail.set_next(new_node)  # (last node in chain).next_node = new_node
            # update the "self.tail" to point to the new node that we just added
            self.tail = new_node

    def remove_tail(self):
        if not self.head and not self.tail:
            return None
        if  self.head == self.tail:
            value = self.tail.get_value()
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



class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if not self.storage.head:
            return
        else:
            value = self.storage.head.get_value()
            self.storage.remove_head()
            self.size -= 1
            return value
