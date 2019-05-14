class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    # if lenth of list equals zero add item to list
    if self.len() == 0:
      self.storage += [item]
    elif self.len() > 0:
      # else append zero to list
      self.storage += [0]
      # loop through list backwards
      for i in range(self.len()-1, 0, -1):
        # switch current val with future val
        self.storage[i], self.storage[i-1] = self.storage[i-1], self.storage[i]
      # add item to index zero in list
      self.storage[0] = item

  def dequeue(self):
    # if lenth of list equals zero return
    if self.len() == 0:
      return
    else:
      # else store last item in list
      result = self.storage[self.len()-1]
      # delete last item 
      del self.storage[self.len()-1]
      # return the stored value
      return result

  def len(self):
    return len(self.storage)
