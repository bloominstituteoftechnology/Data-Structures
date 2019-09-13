
class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    print("Init..")
    self.storage = []

  def enqueue(self, item):
     self.storage.append(item)

  def dequeue(self):

      if len(self.storage):
        return self.storage.pop(0)


  def len(self):
      return len(self.storage)

  def __repr__(self):
      return "Storage : " + (self.storage) + "\n size:  " + len(self.storage)

q = Queue()
print(q.enqueue(5))
print(q.storage)
print (q.dequeue())