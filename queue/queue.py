class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  #enqueue should add an item to the back of the queue.
  def enqueue(self, item):
    self.storage.append(item)
  
  #should remove and return an item from the front of the queue
  def dequeue(self):
    #check if there are items
    if not self.storage:
      return None
    #remove item at first position
    remove_item = self.storage[0]

    self.storage.remove(self.storage[0])
    return remove_item

  #len returns the number of items in the queue
  def len(self):
    count = 0

    for items in self.storage:
      count += 1
    
    return count
