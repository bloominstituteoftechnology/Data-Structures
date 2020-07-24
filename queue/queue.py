import sys
sys.path.insert(0,"/Volumes/TimeMachine/dev/lambda-cs/CS_Wk2/Data-Structures/singly_linked_list/singly_linked_list.py")
from singly_linked_list import LinkedList

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage
structure. Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement
the Queue? What would that look like? How many Stacks would you need? Try it!
"""


class Queue:

    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.insert(0, value)
        self.size += 1

    def dequeue(self):
        if self.storage:
            return self.storage.pop()
        return None

# A linked list node to store a stack entry


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

# A class representing singly linked lists implemented as a queue.
# The front  node stores the front node of the linked list and
# the rear node stores the last node of the linked list.


class QueueLinkedList:
    def __init__(self):
        self.front = self.rear = None

    def __len__(self):
        """ Counts the number of nodes in the linked list iteratively.
        """
        temp_value = self.front
        count = 0
        while(temp_value):
            count += 1
            temp_value = temp_value.next
        return count

    def isEmpty(self):
        """ Determines if linked list is empty.
        """
        return self.front is None

    def enqueue(self, value):
        """ Adds an item to the queue.
        """
        temp_value = Node(value)

        if self.rear is None:
            self.front = self.rear = temp_value
            return
        self.rear.next = temp_value
        self.rear = temp_value

    def dequeue(self):
        """ Removes an item from the queue. It removes the front node and
        moves `front` to the next node"""
        if self.isEmpty():
            return
        temp_value = self.front
        self.front = temp_value.next

        if(self.front is None):
            self.rear = None


#q = QueueLinkedList()
#q.enqueue(10)
#q.enqueue(20)
#q.dequeue()
#q.dequeue()
#q.enqueue(30)
#q.enqueue(40)
#q.enqueue(50)
#q.enqueue(60)
#q.enqueue(70)
#q.dequeue()
#
#print("Queue Length: " + str(len(q)))
#print("Queue Front: " + str(q.front.value))
#print("Queue Rear: " + str(q.rear.value))
