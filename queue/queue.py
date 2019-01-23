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
    # create the new node - new node created in add_to_tail
    # add the ned node to the linkedlist add_to_tail
    # increment size
    pass
  
  def dequeue(self):
    self.storage.remove_head()
    if self.size != 0:
      self.size -= 1
    # remove first element
    # decrement size
    pass

  def len(self):
    return self.size
    # create a counter
    # step through elements incrementing counter
    # return counter
    # -------------------------------
    # or just return self.size

# newQ = Queue()
# print(newQ)
# newQ.enqueue(3)
# newQ.enqueue(5)
# newQ.enqueue(8)
# print(newQ.storage.head.value)
# print(newQ.storage.tail.value)
# newQ.dequeue()
# print(newQ.storage.head.value)
# print(newQ.storage.tail.value)
# print(newQ.len())
