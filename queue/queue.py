import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    #add item back of queue 
    self.size += 1
    self.storage.add_to_tail(item)
   
    
  
  def dequeue(self):
    #removing and return an item from the front of the queue.
    if self.storage.head != None:
      self.size -=1
    return self.storage.remove_head()

  def len(self):
    #here return number of items in queue
    return self.size
