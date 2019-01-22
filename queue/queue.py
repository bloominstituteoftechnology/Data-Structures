import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    # insert item into the add_to_tail method to add
    self.storage.add_to_tail(item)
  
  def dequeue(self):
    return  self.storage.remove_head()

  def len(self):
    # to get the length check first check if there is a length
    # get the value of the current head
    cur_head = self.storage.head
    # check if current head exist
    if cur_head == None:
      return 0
    # check if current head next_node exist
    if cur_head.get_next() == None:
      return 1
    else:
      count = 1

      #and while there are still nodes in the linked list
      while cur_head.get_next() != None:

        # increment count and set the current_head to the next node
        count += 1
        cur_head = cur_head.get_next()

      # set the size to the current value of count and return it to the caller
      self.size = count
      return self.size
      
    # if all conditions fall out then just return the current size to the caller
    return self.size