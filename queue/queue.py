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
    # grab the current head
    current_head = self.storage.head

    # if there is no current head
    if current_head == None:

      # set the size to zero and return the size to the caller
      self.size = 0
      return self.size

    # if there is no next node from the current head
    if current_head.get_next() == None:

      # set size to 1 and return the size to the caller
      self.size = 1
      return self.size
    else:

      # otherwise create a count variable initialize it to 1
      count = 1

      #and while there are still nodes in the linked list
      while current_head.get_next() != None:

        # increment count and set the current_head to the next node
        count += 1
        current_head = current_head.get_next()

      # set the size to the current value of count and return it to the caller
      self.size = count
      return self.size
      
    # if all conditions fall out then just return the current size to the caller
    return self.size

# some debug tests
# q = Queue()

# q.enqueue(2)
# q.enqueue(4)
# q.enqueue(100)
# q.enqueue(1)

# print(q.storage.get_max())
# print(q.dequeue())