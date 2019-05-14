import sys
from linked_list import LinkedList




class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.size += 1
    #add to queue and increment by 1 in every enqueque 
  
  def dequeue(self):
    dq = self.storage.remove_from_head()
    if self.size > 0 :
      self.size -= 1
    return dq    
   # as long as size is not 0 decrement by 1  
  def len(self):
    return self.size
    #returns size of queue
