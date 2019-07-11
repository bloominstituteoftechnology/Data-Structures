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
     temp = self.storage[:1].pop()
     self.storage.pop(0)
     return temp

  def len(self):
   return len(self.storage)


new_Queue = Queue()

new_Queue.enqueue(100)

new_Queue.enqueue(101)

new_Queue.enqueue(105)

new_Queue.dequeue()

def printer(struct):
 for x in struct.storage:
  print(x)

# print('dequeue test', new_Queue.dequeue())

print(printer(new_Queue))