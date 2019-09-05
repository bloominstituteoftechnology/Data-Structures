class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
        self.storage.insert(self.size, item)
        self.size += 1
        # print(self.size)
        # return self.size
    # pass

  def dequeue(self):
    # pass
    if self.size > 0:
      self.size -= 1
      return self.storage.pop(0)


  def len(self):
    # pass
    return self.size


new_Queue = Queue()

new_Queue.enqueue(4)