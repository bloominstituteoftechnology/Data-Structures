class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = list()

  def __str__(self):
    return f"{self.storage}"

  def enqueue(self, item):
    self.storage.append(item)
  
  def dequeue(self):
    if len(self.storage) > 0:
      return self.storage.pop(0)

  def len(self):
    return len(self.storage)
'''
queue = Queue()

queue.dequeue()

queue.enqueue(5)
queue.enqueue(8)
queue.enqueue(13)

print(queue.len(), queue)

queue.dequeue()

print(queue.len(), queue)

queue.enqueue(5)
queue.enqueue(8)

print(queue.len(), queue)

queue.dequeue()

print(queue.len(), queue)
'''