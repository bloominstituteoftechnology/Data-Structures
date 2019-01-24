import sys
sys.path.append('../linked_list')
from linked_list import LinkedList # pylint: disable-msg=E0611

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.size += 1
  
  def dequeue(self):
    if self.size > 0:
      self.size -= 1
      return self.storage.remove_head()
    

  def len(self):
    return self.size


# testQueue = Queue()

# print(testQueue.size)

# testQueue.enqueue('hello')
# print(testQueue.size)
# testQueue.enqueue('hello1')
# print(testQueue.size)
# testQueue.enqueue('hello2')
# print(testQueue.size)
# print(testQueue.dequeue())
# print(testQueue.size)
# print(testQueue.dequeue())
# print(testQueue.dequeue())
# print(testQueue.dequeue())
# print(testQueue.dequeue())
# print(testQueue.size)