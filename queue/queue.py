class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = [] 

  def enqueue(self, item):
    self.storage.append(item)
    return self.storage
  
  def dequeue(self):
    if not self.storage:
      return
    else:
      removed = self.storage.pop(0)
      return int(removed)

  def len(self):
    return int(len(self.storage))
