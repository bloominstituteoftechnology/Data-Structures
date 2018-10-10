import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    # Increases the size by 1 and adds item to tail of queue
    self.size += 1
    self.storage.add_to_tail(item)

  def dequeue(self):
    # If the queue is empty, returns None since you can't remove nothing
    if self.size == 0:
        return None
    # Decreases the size by 1 and removes the head of the queue
    self.size -= 1
    return self.storage.remove_head()

  def len(self):
    # Returns the size of the queue, which is how many elements/nodes(?) are in it
    return self.size
