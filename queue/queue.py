class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.storage.append(item)
  
  
  def dequeue(self):
    if self.len() > 0:
      print(self.storage.pop(0))

  def len(self):
    return len(self.storage)


q = Queue()
q.enqueue(100)
q.enqueue(101)
q.enqueue(105)
q.dequeue()
