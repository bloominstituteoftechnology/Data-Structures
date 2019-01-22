import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  # O(1)
  def enqueue(self, item):
    # Adds item to tail
    self.storage.add_to_tail(item)  # O(1)
    # Increments size
    self.size += 1  # O(1)

  # O(1)
  def dequeue(self):
    # Checks if storage is empty
    if self.storage.head is not None:
      # If not, increments size and removes head
      self.size -= 1  # O(1)
      return self.storage.remove_head()
    else:
      # If it is, returns None
      return None

  # O(1)
  def len(self):
    # Simply returns the queue's size
    return self.size  # O(1)
