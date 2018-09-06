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
    self.storage.remove_head()
    pass

  def len(self):
    pass



queue1 = Queue()

queue1.enqueue(Node(1))
queue1.enqueue(Node(5))

print(queue1.storage.head.value)
print(queue1.storage.tail.value)
queue1.dequeue()

print()
