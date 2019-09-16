
class Queue:
  def __init__(self):
    self.storage = []

  def enqueue(self, item):
    self.storage.append(item)
    # this will add item as the next item in the storage list
    
  
  def dequeue(self):
    #if length is greater than 0, pop off the last item:
    if len(self.storage) > 0:
      return self.storage.pop(0)
    return None #return None when the length is 0

  def len(self):
    # return len(self.storage)
    return len(self.storage)
