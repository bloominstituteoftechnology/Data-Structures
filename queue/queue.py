class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.storage.append((item))
    self.size +=1
    pass
  
  def dequeue(self):
    if self.size > 0:
      element = self.storage.pop(0)
      self.size -=1
      return element
    pass

  def len(self):
    return self.size
    pass
