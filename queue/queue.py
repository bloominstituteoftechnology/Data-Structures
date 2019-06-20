class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.storage.append(item)
    
  
  def dequeue(self):
    if len(self.storage) > 1 or len(self.storage) == 1:
     self.storage.remove(0)
    elif len(self.storage) < 1:
     return None 

  def len(self):
   return len(self.storage)
