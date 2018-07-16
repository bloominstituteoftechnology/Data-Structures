import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    if self.storage() >= self.size:
      return ("Queue Full")
      self.queue.append(data)
      self.tail += 1
      return True     

  
  def dequeue(self):
    if self.size() <= 0:
      self.resetQueue()
      return ("Queue Empty") 
      data = self.queue[self.head]
      self.head+=1
      return data

  def len(self):
    return self.tail - self.head
