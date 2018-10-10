import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    return self.storage.add_to_tail(item)
  
  def dequeue(self):
    return self.storage.remove_head()

  def len(self):
    if self.storage.head==None:
      return 0
    else:
      length=1
      node=self.storage.head
      while True:
        if node.get_next()!=None:
          node=node.get_next()
          length+=1
        elif node.get_next()==None:
          break
      return length
