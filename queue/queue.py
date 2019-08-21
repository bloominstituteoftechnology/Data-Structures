class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements? linked list
    self.storage = []

  def enqueue(self, item):
    #adds element to end of queue
    self.storage.insert(0,item)
  
  def dequeue(self):
    #removes element at beginning of queue
    if len(self.storage) < 1:
      return None
    return self.storage.pop()
      
  def len(self):
    return len(self.storage)

