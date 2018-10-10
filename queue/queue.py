import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    #just add the item to the storage using 
    #add to tail, then add 1 to size
    self.storage.add_to_tail(item)
    self.size += 1
  
  def dequeue(self):
    #if the size is greater than 0 then 
    # self.size -= 1 is removing 1 item from the list
    #remove the head of the list using the 
    #remove head function
    if self.size > 0:
      self.size -= 1
    return self.storage.remove_head()

  def len(self):
    #just return the size of the list
    return self.size