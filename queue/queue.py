
import sys
sys.path.append('../linked_list')
from linked_list import LinkedList


class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.size += 1
    print(self)
    if self.storage.tail == None and self.storage.head == None:
    	self.storage.tail = item
    elif self.storage.head == None:
    	self.next_in_line = item
    	self.storage.head = item
    else:
    	self.storage.head = item

  def dequeue(self):
    if self.size == 0:
      return None
    if self.storage.head == None and self.storage.tail == None:
      self.size = 0
      return None
    else:
      self.size = self.size - 1
      val = self.storage.tail

      self.storage.tail = self.next_in_line
      self.next_in_line = self.storage.head
      self.storage.head = None
      return val

  def len(self):
    return self.size
