import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.size += 1
    self.storage.add_to_tail(item)
  
  def dequeue(self):
    self.size -= 1
    return self.storage.remove_head()

  def len(self):
    return self.size

###############
## Test Code ##
###############

# Q = Queue()
# Q.enqueue(1)
# Q.enqueue(3)
# Q.enqueue(5)
# Q.enqueue(7)
# Q.enqueue(9)
# print(Q.dequeue())
# print(Q.len())
# print(Q.dequeue())
# print(Q.len())
