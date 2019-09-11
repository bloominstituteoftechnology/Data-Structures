class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.storage.insert(0, item)
    print("enqueue", self.storage)
    return self.storage

  def dequeue(self):
    if len(self.storage) == 0:
      return
    else:
      updatedList = self.storage.pop(-1)
      return updatedList

  def len(self):
    return len(self.storage)

print(Queue())