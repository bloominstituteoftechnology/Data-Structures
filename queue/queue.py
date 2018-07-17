# import sys
# sys.path.append('../linked_list')
# from linked_list import LinkedList


class Queue:
  def __init__(self):
    self.size = 0
    self.storage = list()

  def enqueue(self, item):
    self.storage.append(item)
    self.size += 1

  def dequeue(self):
    if self.size == 0:
      return None
    else:
      result = self.storage.pop(0)
      self.size -= 1
    return result

  def len(self):
    if self.storage == 0:
      return None
    return self.size
