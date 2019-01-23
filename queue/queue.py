import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.size += 1
  
  def dequeue(self):
    self.storage.remove_head()
    self.size -= 1

  def len(self):
    return self.size

q = Queue()
print(q.len())
q.enqueue(1)
print(q.len())
q.enqueue(2)
print(q.len())
q.enqueue(3)
print(q.len())
q.enqueue(4)
print(q.len())
q.enqueue(5)
print(q.len())
q.enqueue(6)
print(q.len())
q.enqueue(7)
print(q.len())
q.enqueue(8)
print(q.len())
q.enqueue(9)
print(q.len())

