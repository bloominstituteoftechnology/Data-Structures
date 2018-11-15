import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.size +=1
  
  def dequeue(self):
    if self.size == 0:
      return None
    else:
      self.size -= 1
      return self.storage.remove_head()

  def len(self):
    return self.size
    # current_node = self.storage.head
    # if self.storage.head == None:
    #   self.size = 0
    #   return 0
    # elif self.storage.head == self.storage.tail:
    #   self.size = 1
    #   return 1
    # else:
    #   count = 0
    #   while current_node != None:
    #     count +=1
    #     current_node = current_node.get_next()
    #   self.size = count
    #   return count