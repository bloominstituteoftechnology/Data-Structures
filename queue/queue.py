from singly_linked_list import Node, LinkedList

# Implement the Stack and Queue classes using built-in Python lists
# and the Node and LinkedList classes you created during the
# Module 1 Guided Project.

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

# Has the methods: enqueue, dequeue, and len.
# enqueue adds an element to the back of the queue.
# dequeue removes and returns the element at the front of the queue.
# len returns the number of elements in the queue.

# # Array implementation of Queue class
# class Queue:
#     """Array implementation of Queue class"""
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         """Returns the number of elements in the queue"""
#         return self.size

#     def enqueue(self, value):
#         """Adds an element to the back of the queue"""
#         self.storage.append(value)
#         self.size = len(self.storage)

#     def dequeue(self):
#         """Removes and returns the element at the front of the queue"""
#         # if empty
#         if self.size == 0:
#             return None
#         else:
#             front = self.storage[0]
#             self.storage.remove(front)
#             self.size = len(self.storage)
#             return front


# OOP implementation of Queue class
class Queue:
    """OOP implementation of Queue class using Node and LinkedList classes"""

    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        """Returns the number of elements in the queue"""
        count = 0
        current = self.storage.head
        # loop through to count "heads"
        while current:
            current = current.get_next()
            count += 1
        self.size = count
        return count

    def enqueue(self, value):
        """Adds an element to the back of the queue"""
        self.storage.add_to_tail(value)
        count = 0
        current = self.storage.head
        # loop through to count "heads"
        while current:
            current = current.get_next()
            count += 1
        self.size = count

    def dequeue(self):
        """Removes and returns the element at the front of the queue"""
        if self.size == 0:
            return None
        else:
            front = self.storage.head.get_value()
            self.storage.remove_head()
            return front
        count = 0
        current = self.storage.head
        # loop through to count "heads"
        while current:
            current = current.get_next()
            count += 1
        self.size = count
