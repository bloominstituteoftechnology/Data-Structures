import sys
sys.path.append('../linked_list')
from linked_list import LinkedList
from linked_list import Node

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item): #INSERT operation
    self.storage.add_to_tail(item)
    pass
  
  def dequeue(self): #DELETE operation
    if self.storage.head == None:
      return None
    else:
      oldHead = self.storage.head.value
      self.storage.remove_head()
    return oldHead

  def len(self):
    currentNode = self.storage.head
    if currentNode == None:
      self.size = 0
      return self.size
    if currentNode.get_next() == None:
      self.size = 1
      return self.size
    else:
      counter = 1
      while currentNode.get_next() != None:
        counter += 1
        currentNode = currentNode.get_next()
      self.size = counter
      return self.size





# queue1 = Queue()

# queue1.enqueue(1)
# queue1.enqueue(5)
# queue1.enqueue(15)
# queue1.enqueue(54)

# print(queue1.storage.head.value)
# print(queue1.storage.tail.value)
# queue1.dequeue()

# print(queue1.storage.head.value)

# print(queue1.len())


# queue1.enqueue(100)
# queue1.enqueue(101)
# queue1.enqueue(105)
# print(queue1.dequeue())
# assertEqual(queue1.dequeue(), 100)