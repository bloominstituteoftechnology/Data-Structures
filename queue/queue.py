import sys
sys.path.append('../linked_list')
from linked_list import LinkedList, Node

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    new_node = Node(item)
    if self.storage.head:
      new_node.set_next(self.storage.head)
      self.storage.head = new_node
    else: 
      new_node.set_next(None)
      self.storage.tail = new_node
      self.storage.head = new_node
    pass
  
  def dequeue(self):
    pass

  def len(self):
    if self.storage.head == None:
      return 0 
    else:#will not know if below is correct until enque is complete 
      count = 1 
      x = self.storage.head.get_next()
      while x != None:
        count = count + 1
        x = x.get_next()
      return count
    pass
