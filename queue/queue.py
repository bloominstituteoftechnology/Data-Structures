import sys
sys.path.append('../linked_list')
from linked_list import LinkedList, Node

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    new_node = self.storage.tail
    # print(new_node)
    if self.storage.head == None:
       self.storage.head = item 
    else:
      new_node = item
    new_node = item

  
  def dequeue(self):
    remove_node = self.storage.head
    if self.size == 0:
      return None
    else:

      return self.storage.remove_head()
      # return self.storage.head


  def len(self):
    return self.size



# storage gives access to the whole linked_list
# q = Queue()
# print(vars(q.storage))  head and tail are variables in the dictionary

