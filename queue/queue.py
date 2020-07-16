from llist import LinkedList
from llist import Node
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
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


class Queue(LinkedList):
    def __init__(self):
        super().__init__()
        self.size = 0
        # self.storage = ?

    def __len__(self):
        return self.size

    def enqueue(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def dequeue(self):
        head = self.head
        if not head:
            return None
        else:
            self.size -= 1
            self.head = head.next
            return head.value


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(505)
q.print_list()
print('length', len(q))
q.dequeue()
print(len(q))
