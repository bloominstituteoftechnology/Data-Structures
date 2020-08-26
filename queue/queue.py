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
   Using an array we would only be able to do first in first out as thats the only way it works. The biggest difference is there isn't any order in the array, but in a linked list there is a specific order depending on where the node is pointing to so it can be much longer than in an array, which is fixed.
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.insert(0,value)

    def dequeue(self):
      if self.__len__() is 0:
         return None
      else:
         return self.storage.pop()

# from singly_linked_list.singly_linked_list import LinkedList
# class Queue:
#    def __init__(self):
#       self.size = 0
#       self.storage = LinkedList()
   
#    def __len__(self):
#       return self.size

#    def enqueue(self, value):
#       self.storage.add_to_head(value)
#       self.size += 1

#    def dequeue(self):
#       if self.__len__() is 0:
#          return None
#       else:
#          front = self.storage.remove_from_tail()
#          self.size -= 1
#          return front.value