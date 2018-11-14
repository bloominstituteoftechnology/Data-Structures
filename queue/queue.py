import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    # add the item to the tail of the storage of the queue
    self.storage.add_to_tail(item)
  
  def dequeue(self):
    # if there is no node in the storage
    if self.storage.head == None:
      # return none to the caller
      return None
    else:
      # otherwise take the previous head from storage and remove it
      previous_head = self.storage.head.value
      self.storage.remove_head()
    # return the previous head to the caller
    return previous_head

  def len(self):
    # TODO: do some length / size setting in this method with some logic after a coffee break
    return self.size

# some debug tests
q = Queue()

q.enqueue(2)
q.enqueue(4)
q.enqueue(100)
q.enqueue(1)

print(q.storage.get_max())
print(q.dequeue())