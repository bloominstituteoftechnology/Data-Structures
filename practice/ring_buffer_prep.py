# Implement a Ring Buffer Data Structure
"""
A ring buffer is a non-growable buffer with a fixed size. 
When the ring buffer is full and a new element is inserted, the oldest 
element in the ring buffer is overwritten with the newest element. 
This kind of data structure is very useful for use cases such as storing 
logs and history information, where you typically want to store 
information up until it reaches a certain age, after which you don't 
care about it anymore and don't mind seeing it overwritten by newer data.

Implement this behavior in the RingBuffer class. 

RingBuffer has two methods, append and get. 

The append method adds the given element to the buffer. 

The get method returns all of the elements in the buffer in a list in 
their given order. It should not return any None values in the list 
even if they are present in the ring buffer.
"""

class RingBuffer:
    """
    RingBuffer has two methods, append and get. 
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def append(self, item):
        """
        Adds the given element to the buffer.
        """
        # Check size of buffer
        # If buffer size less than capacity, add elem
        if len(self.buffer) < self.capacity:
            # Add item to buffer
            self.buffer.append(item)
        else:
            # Replace oldest item with new item
            # Need oldest item designation to iterate through
            # len(self.capacity)
            self.buffer[0] = item

    def get(self):
        """
        Returns all of the elements in the buffer in a list in 
        their given order.
        """
        pass