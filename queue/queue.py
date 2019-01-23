import sys
sys.path.append('../linked_list')
from linked_list import LinkedList # noqa 
'''Adding # noqa to a line indicates that the linter 
   (a program that automatically checks code quality) 
   should not check this line. 
   Any warnings that code may have generated will be ignored.'''

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
      self.storage.add_to_tail(item)
      self.size += 1
  
  def dequeue(self):
      if self.size > 0:
          self.size -= 1
          return self.storage.remove_head()

  def len(self):
      return self.size
