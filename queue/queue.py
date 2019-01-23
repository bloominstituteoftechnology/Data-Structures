import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    # create the new node
    # add the ned node to the linkedlist add_to_tail
    # increment size
    pass
  
  def dequeue(self):
    # step to the last element
    # remove last element
    # decrement size
    pass

  def len(self):
    # create a counter
    # step through elements incrementing counter
    # return counter
    # -------------------------------
    # or just return self.size
    pass

ll = LinkedList()
ll.add_to_tail(4)
ll.add_to_tail(8)
print(ll.head.value)
print(ll.tail.value)