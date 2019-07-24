class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item): # add an item to the back of the queue
    self.storage.insert(0, item)
    self.size += 1


    
  
  def dequeue(self): # should remove and return an item from the front of the queue.
    if self.size == 0:
      return None
    else:
      self.size -= 1
      return self.storage.pop()

  def len(self): # returns the number of items in the queue
    return self.size
