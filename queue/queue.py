class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    # place object at begining of list
    # increment size property
    self.storage = [item] + self.storage
    self.size += 1
    return self.storage
  
  def dequeue(self):
    # remove item from end of list
    # decrement size property
    # return dequeue
    if len(self.storage) > 0:
        popped = self.storage.pop()
        self.size -= 1
        return popped

    return None    

  def len(self):
      return self.size
